from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os
from google.cloud import storage

app = FastAPI()

# Descargar el modelo desde GCS cuando se inicie la aplicación
BUCKET_NAME = os.environ.get('BUCKET_NAME')
MODEL_PATH = os.environ.get('MODEL_PATH')
LOCAL_MODEL_PATH = '/tmp/iris_model.joblib'

if not os.path.exists(LOCAL_MODEL_PATH):
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(MODEL_PATH)
    blob.download_to_filename(LOCAL_MODEL_PATH)

model = joblib.load(LOCAL_MODEL_PATH)

# Define la estructura de datos que esperamos para la predicción
class Item(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Un endpoint para verificar que el servicio está funcionando
@app.get("/health")
def health_check():
    return {"status": "ok"}

# El endpoint principal para realizar predicciones
@app.post("/predict")
def predict(item: Item):
    data = [[item.sepal_length, item.sepal_width, item.petal_length, item.petal_width]]
    prediction = model.predict(data)
    return {"prediction": int(prediction[0])}