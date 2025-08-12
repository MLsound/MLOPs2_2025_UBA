import collections
import numpy as np
import tensorflow as tf
import tensorflow_federated as tff
import matplotlib.pyplot as plt

# ---- 1) Cargar y preprocesar datos EMNIST ----
emnist_train, emnist_test = tff.simulation.datasets.emnist.load_data()

NUM_CLIENTS = 10
BATCH_SIZE = 32
ROUNDS = 50
NUM_EPOCHS = 5

def create_client_data(client_id):
    return emnist_train.create_tf_dataset_for_client(client_id)

def preprocess_dataset(dataset):
    def flatten_and_normalize(element):
        image = tf.cast(element['pixels'], tf.float32) / 255.0
        image = tf.reshape(image, [-1])
        label = tf.cast(element['label'], tf.int32)
        return image, label
    
    return dataset.map(flatten_and_normalize).repeat(NUM_EPOCHS).batch(BATCH_SIZE).prefetch(tf.data.AUTOTUNE)

client_ids = emnist_train.client_ids[:NUM_CLIENTS]
federated_train_data = [preprocess_dataset(create_client_data(cid)) for cid in client_ids]

# ---- Dataset de prueba (global) ----
test_dataset = emnist_test.create_tf_dataset_from_all_clients()
test_dataset = preprocess_dataset(test_dataset)

# ---- 2) Modelo Keras ----
def create_keras_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Input(shape=(784,)),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    return model

def model_fn():
    keras_model = create_keras_model()
    return tff.learning.models.from_keras_model(
        keras_model,
        input_spec=federated_train_data[0].element_spec,
        loss=tf.keras.losses.SparseCategoricalCrossentropy(),
        metrics=[tf.keras.metrics.SparseCategoricalAccuracy()]
    )

# ---- 3) Algoritmo FedAvg ----
iterative_process = tff.learning.algorithms.build_weighted_fed_avg(
    model_fn,
    client_optimizer_fn=tff.learning.optimizers.build_sgdm(learning_rate=0.5),
    server_optimizer_fn=tff.learning.optimizers.build_sgdm(learning_rate=1.0),
    client_weighting=tff.learning.ClientWeighting.NUM_EXAMPLES,
)

# ---- 4) Evaluación global y por clase ----
def evaluate_model(state):
    keras_model = create_keras_model()
    model_weights = iterative_process.get_model_weights(state)
    model_weights.assign_weights_to(keras_model)
    
    acc = tf.keras.metrics.SparseCategoricalAccuracy()
    loss = tf.keras.metrics.SparseCategoricalCrossentropy()
    per_class_acc = {i: [0, 0] for i in range(10)}

    for x, y in test_dataset:
        preds = keras_model(x, training=False)
        acc.update_state(y, preds)
        loss.update_state(y, preds)
        y_pred = tf.argmax(preds, axis=1)
        for label, pred in zip(y.numpy(), y_pred.numpy()):
            per_class_acc[int(label)][1] += 1
            if label == pred:
                per_class_acc[int(label)][0] += 1

    per_class_acc_pct = {cls: (hits / total if total > 0 else 0.0)
                         for cls, (hits, total) in per_class_acc.items()}
    return acc.result().numpy(), loss.result().numpy(), per_class_acc_pct

# ---- 5) Función para imprimir métricas por ronda ----
def print_metrics(round_num, metrics, eval_acc, eval_loss):
    tm = metrics['client_work']['train']
    print(f"Ronda {round_num:2d} | "
          f"Train Acc: {tm['sparse_categorical_accuracy']:.4f} | "
          f"Train Loss: {tm['loss']:.4f} | "
          f"Eval Acc: {eval_acc:.4f} | "
          f"Eval Loss: {eval_loss:.4f} | "
          f"Ejemplos: {tm['num_examples']}")

# ---- 6) Preparar dataset envenenado ----
def poison_raw_dataset(raw_ds):
    def swap_labels(elem):
        image = elem['pixels']
        label = tf.cast(elem['label'], tf.int32)
        label = tf.where(tf.equal(label, 3), tf.constant(7, dtype=tf.int32), label)
        label = tf.where(tf.equal(label, 7), tf.constant(3, dtype=tf.int32), label)
        return {'pixels': image, 'label': label}
    return raw_ds.map(swap_labels)

poisoned_federated_train_data = list(federated_train_data)
raw_client0 = create_client_data(client_ids[0])
poisoned_raw0 = poison_raw_dataset(raw_client0)
poisoned_federated_train_data[0] = preprocess_dataset(poisoned_raw0)

# ---- 7) Entrenamiento y registro de métricas ----
results_clean = []
results_poison = []

print("--- Entrenamiento SIN Ataque ---")
state = iterative_process.initialize()
for round_num in range(1, ROUNDS + 1):
    result = iterative_process.next(state, federated_train_data)
    state = result.state
    eval_acc, eval_loss, _ = evaluate_model(state)
    print_metrics(round_num, result.metrics, eval_acc, eval_loss)
    results_clean.append(eval_acc)

print("\n--- Entrenamiento CON Ataque de Envenenamiento (cliente 0) ---")
state_poison = iterative_process.initialize()
for round_num in range(1, ROUNDS + 1):
    result = iterative_process.next(state_poison, poisoned_federated_train_data)
    state_poison = result.state
    eval_acc, eval_loss, per_class_acc = evaluate_model(state_poison)
    print_metrics(round_num, result.metrics, eval_acc, eval_loss)
    if round_num == ROUNDS:
        print("\nPrecisión por clase en última ronda (con ataque):")
        for cls in range(10):
            print(f"Clase {cls}: {per_class_acc[cls]:.4f}")
    results_poison.append(eval_acc)

# ---- 8) Gráfico de precisión global ----
plt.figure(figsize=(8,5))
plt.plot(range(1, ROUNDS+1), results_clean, label="Sin ataque")
plt.plot(range(1, ROUNDS+1), results_poison, label="Con ataque", linestyle='--')
plt.xlabel("Ronda")
plt.ylabel("Precisión global en test")
plt.title("Efecto del envenenamiento de datos")
plt.legend()
plt.grid(True)
plt.savefig("/app/envenenamiento_precision.png")