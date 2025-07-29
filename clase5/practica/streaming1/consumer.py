import json
import joblib
from kafka import KafkaConsumer
import pandas as pd
import numpy as np

# Cargar el modelo pre-entrenado
model = joblib.load('ml_model/simple_model.pkl')
print("Modelo de ML cargado exitosamente.")

# Configuración del consumidor Kafka
consumer = KafkaConsumer(
    'sensor_data',
    bootstrap_servers=['localhost:9094'], # Usar el puerto expuesto por Docker Compose
    auto_offset_reset='earliest', # Empieza a leer desde el principio si no hay offset guardado
    enable_auto_commit=True,
    group_id='ml-processing-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Escuchando mensajes en el tópico 'sensor_data'...")

try:
    for message in consumer:
        data = message.value
        print(f"Received: {data}")

        # Simular preprocesamiento de features
        # Para nuestro modelo simple, usaremos temperatura y humedad como features
        features = np.array([[data['temperature'], data['humidity']]])
        
        # Realizar inferencia
        prediction = model.predict(features)[0]
        prediction_proba = model.predict_proba(features)[0].tolist()

        print(f"  Processed features: {features.tolist()}")
        print(f"  Prediction: {'Anomalía' if prediction == 1 else 'Normal'}")
        print(f"  Prediction probabilities: {prediction_proba}")
        print("-" * 30)

except KeyboardInterrupt:
    print("Deteniendo consumidor...")
finally:
    consumer.close()
    print("Consumidor cerrado.")