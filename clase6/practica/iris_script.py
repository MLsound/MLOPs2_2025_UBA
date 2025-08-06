import pandas as pd
from sklearn import datasets

# 1. Cargar el dataset de Iris en memoria
iris = datasets.load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

# 2. Guardar el dataset en un archivo local
file_path = "iris_raw.csv"
df.to_csv(file_path, index=False)

print(f"Dataset guardado localmente en {file_path}")
print("Primeras 5 filas del dataset:")
print(df.head())