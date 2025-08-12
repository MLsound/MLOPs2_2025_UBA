# Usa una imagen base de Python oficial
FROM python:3.10-slim

# Instala Poetry
RUN pip install poetry

# Establece el directorio de trabajo
WORKDIR /app

# Copia solo el archivo de configuración principal de Poetry
# 'pyproject.toml' debe existir en tu carpeta local.
COPY pyproject.toml .

# Instala las dependencias y genera el poetry.lock dentro del contenedor
RUN poetry install --no-root

# Copia el script del tutorial
COPY tutorial_federado.py .

# Define el comando para ejecutar el script
CMD ["poetry", "run", "python", "tutorial_federado.py"]