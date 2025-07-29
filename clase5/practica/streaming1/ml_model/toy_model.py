import joblib
from sklearn.linear_model import LogisticRegression
import numpy as np

# Datos dummy para entrenar un modelo simple
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]])
y = np.array([0, 0, 0, 1, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)

# Guardar el modelo en la ruta esperada por el consumidor
joblib.dump(model, 'simple_model.pkl')
print("Modelo simple guardado como streaming1/ml_model/simple_model.pkl")