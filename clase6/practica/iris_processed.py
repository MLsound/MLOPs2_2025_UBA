import pandas as pd
from google.cloud import storage

# 1. Define tu bucket y las rutas de los archivos
BUCKET_NAME = "mlops-data-lake-tutorial-654"  # Reemplaza con el nombre de tu bucket
RAW_FILE_PATH = "raw/iris_data/iris_raw.csv"
CURATED_FILE_PATH = "curated/iris_data/iris_processed.csv"

# 2. Descargar el archivo crudo desde GCS
client = storage.Client()
bucket = client.bucket(BUCKET_NAME)
blob = bucket.blob(RAW_FILE_PATH)
blob.download_to_filename("iris_raw.csv")

# 3. Leer y procesar los datos con Pandas
df_raw = pd.read_csv("iris_raw.csv")
df_processed = df_raw.rename(columns={
    'sepal length (cm)': 'sepal_length',
    'sepal width (cm)': 'sepal_width',
    'petal length (cm)': 'petal_length',
    'petal width (cm)': 'petal_width'
})

# 4. Guardar los datos procesados localmente
df_processed.to_csv("iris_processed.csv", index=False)

# 5. Subir el archivo procesado a la carpeta 'curated' en GCS
blob = bucket.blob(CURATED_FILE_PATH)
blob.upload_from_filename("iris_processed.csv")

print("Datos procesados y subidos a la capa 'curated' del Data Lake.")
