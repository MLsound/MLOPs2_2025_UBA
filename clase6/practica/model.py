import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from google.cloud import storage
import pandas as pd

# 1. Define tu bucket y el archivo de datos procesados
BUCKET_NAME = "mlops-data-lake-tutorial-654" # Reemplaza con el nombre de tu bucket
CURATED_FILE_PATH = "curated/iris_data/iris_processed.csv"

# 2. Descargar los datos procesados para el entrenamiento
client = storage.Client()
bucket = client.bucket(BUCKET_NAME)
blob = bucket.blob(CURATED_FILE_PATH)
blob.download_to_filename("iris_processed.csv")

# 3. Preparar los datos para el modelo
df_curated = pd.read_csv("iris_processed.csv")
X = df_curated.drop(columns=['target'])
y = df_curated['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Entrenar el modelo de Machine Learning
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Guardar el modelo entrenado localmente
model_filename = 'iris_model.joblib'
joblib.dump(model, model_filename)

print("Modelo entrenado y guardado localmente.")

# 6. Subir el modelo a una carpeta versionada en GCS
VERSION = 'v1.0' # Esta es la versión de nuestro modelo
MODEL_GCS_PATH = f"models/{VERSION}/{model_filename}"
blob = bucket.blob(MODEL_GCS_PATH)
blob.upload_from_filename(model_filename)

print(f"Modelo versionado subido a: gs://{BUCKET_NAME}/{MODEL_GCS_PATH}")
