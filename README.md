[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

# Operaciones de Aprendizaje Automático I
Este repositorio contiene el material de clases (presentaciones, ejercicios y notebooks) para Operaciones de Aprendizaje Automático II (CEIA - FIUBA). 

Para revisar los criterios de aprobación, ver el [documento correspondiente](CriteriosAprobacion.md).

### Objetivo de la materia
El objetivo de la materia es acercar a los alumnos los conceptos necesarios para desarrollar productos de software relacionados a Machine Learning y análisis de datos de una manera escalable y siguiendo buenas prácticas de programación. También se trabaja sobre las tareas operativas de Machine Learning (MLOps) con distintas herramientas para disponibilizar los resultados en ambientes productivos.

El curso "Operaciones de Aprendizaje Automático II" busca proporcionar a los estudiantes los conceptos y herramientas necesarias para desarrollar productos de software relacionados con Machine Learning y análisis de datos de manera escalable y siguiendo buenas prácticas de programación. También aborda las tareas operativas de Machine Learning (MLOps) utilizando diversas herramientas para disponibilizar los resultados en entornos productivos.

Este curso es la continuación de [Operaciones de Aprendizaje Automático I](https://github.com/FIUBA-Posgrado-Inteligencia-Artificial/aprendizaje_maquina_II). Los temas de MLOps II se centran en el flujo de datos (bases de datos, API REST, transporte en tiempo real), protocolos como GraphQL y gRPC, Aprendizaje Federado, Streaming, Procesamiento en la nube y Seguridad en IA. Se imparte en 8 encuentros de 3 horas cada uno.

El material del curso incluye presentaciones, ejercicios y notebooks, y se espera que los estudiantes utilicen Python, Poetry/Pip/Conda, MLflow, Jupyter Notebook, GitHub, Docker y Apache Airflow. La evaluación se realiza a través de un trabajo práctico final grupal, donde los estudiantes deben implementar un ciclo de desarrollo y despliegue de modelos de Machine Learning, con opciones de implementación local o en contenedores.

### Organización del Repositorio
``` 
    clase#
        teoria
        hands-on
        README.md
```

### Requerimientos
* Lenguaje de Programación
    * Python >=3.10
    * Poetry / Pip / Conda para instalar librerías
* Librerías
    * MLflow
    * Librerias de manejo de datos y de modelos de aprendizaje automático.
    * Jupiter Notebook
* Herramientas
    * GitHub para repositorios
    * Docker
    * Apache Airflow
* IDE Recomendados 
    * Visual Studio Code
    * PyCharm Community Edition    

#### Poetry
Este repositorio contiene un archivo `pyproject.toml` para instalar las dependencias usando 
[Poetry](https://python-poetry.org/)

## Contenido
 
### [Clase 1 - Modos de Flujo de Datos y Patrones Avanzados de APIs REST ](clase1/README.md) 

Contenido Teórico (Repaso y Profundización):

* Recap de los modos de flujo de datos en MLOps (bases de datos, APIs REST, transporte en tiempo real).
* Diseño de APIs REST para servicios de modelos de ML: buenas prácticas, versionado de APIs.
* Patrones de comunicación sincrónica (online prediction) vs. asincrónica (batch prediction) en entornos de ML.
* Manejo de estados y escalabilidad en APIs de ML.

Contenido Práctico:

* Validación de datos de entrada en FastAPI.
* Implementación de endpoints para predicción en línea y en lote.
* Creación de un cliente básico para interactuar con la API.
* Discusión sobre los desafíos del despliegue y monitoreo de estas APIs.

### [Clase 2 - GraphQL en MLOps - Flexibilidad en la Consulta de Datos](clase2/README.md) 

Contenido Teórico:

* Introducción a GraphQL: diferencia con REST, ventajas y desventajas.
* Conceptos clave: Schema Definition Language (SDL), Queries, Mutations, Subscriptions, Resolvers.
* Casos de uso de GraphQL en MLOps
* Consulta flexible de metadatos de experimentos y modelos (ej. desde MLflow).
* Agregación de datos de múltiples servicios de MLOps.

Contenido Práctico:

* Implementación de un servicio GraphQL básico con FastAPI (utilizando librerías como strawberry o graphene).
* Definición de un esquema GraphQL para exponer información (simulada) de experimentos de MLflow.
* Realización de queries y mutations desde un cliente GraphQL (ej. GraphiQL).

### [Clase 3 - gRPC para Microservicios de ML de Alta Performances](clase3/README.md) 
Contenido Teórico:

* Introducción a gRPC: RPC (Remote Procedure Call), Protocol Buffers.
* Modelos de comunicación: Unary, Server Streaming, Client Streaming, Bidirectional Streaming.
* Ventajas de gRPC: eficiencia, performance, contrato de servicio estricto.
* Casos de uso en MLOps: comunicación interna entre microservicios (ej. preprocesamiento de datos, inferencia de baja latencia), comunicación entre lenguajes.
* Comparación detallada entre REST, GraphQL y gRPC para diferentes escenarios de MLOps.

Contenido Práctico:

* Definición de un archivo .proto para un servicio de inferencia de ML.
* Generación de código cliente y servidor gRPC.
* Implementación de un servicio gRPC simple para realizar predicciones con un modelo.
* Desarrollo de un cliente gRPC para interactuar con el servicio.

### [Clase 4 - Procesamiento de Datos en Streaming para Machine Learning](clase4/README.md) 
Contenido Teórico:

* Conceptos de procesamiento de streaming: eventos, colas de mensajes, arquitecturas event-driven.
* Herramientas comunes para streaming de datos (Kafka, Redis Streams, Spark Streaming, Flink - a alto nivel).
* Patrones de MLOps con streaming: inferencia en tiempo real, monitoreo continuo de modelos, reentrenamiento adaptativo.
* Desafíos en el procesamiento de streaming (latencia, consistencia, tolerancia a fallos).

Contenido Práctico:

* Configuración básica de una cola de mensajes (ej. Redis Streams o Kafka simulado con Docker Compose).
* Desarrollo de un "productor" que envíe datos de transacciones simuladas al stream.
* Implementación de un "consumidor" que lea datos del stream, realice inferencia en tiempo real con un modelo pre-entrenado y guarde los resultados.

### [Clase 5 - Procesamiento en la Nube y Data Lakes para MLOps](clase5/README.md) 
Contenido Teórico:

* Introducción a las arquitecturas de MLOps en la nube: servicios de compute, storage, networking.
* Concepto de Data Lake y su rol en MLOps.
* Proveedores de Data Lakes en la nube (Amazon S3, Azure Data Lake Storage, Google Cloud Storage).
* Profundización en MinIO como un Data Lake compatible con S3 para entornos locales y desarrollo.
* Estrategias de despliegue de modelos en la nube (ej. servicios gestionados como AWS SageMaker, Google Cloud Vertex AI, Azure ML - enfoque conceptual).

Contenido Práctico:

* Integración avanzada de MinIO con Airflow y MLflow para la gestión de datos, modelos y artefactos.
* Ejemplos de cómo una pipeline de Airflow interactúa con MinIO para ETL y carga de datos para entrenamiento.
* Cómo el servicio de predicción carga el modelo directamente desde MinIO/S3.
* Discusión sobre la transición de un entorno local containerizado a un despliegue en la nube.

### [Clase 6 - Aprendizaje Federado - Privacidad y Descentralización en ML](clase6/README.md) 
Contenido Teórico:

* Conceptos fundamentales de Aprendizaje Federado (Federated Learning): entrenamiento distribuido sin compartir datos brutos.
* Principios de privacidad: por qué es importante y cómo el Aprendizaje Federado ayuda.
* Arquitecturas de Aprendizaje Federado: clientes, servidor de agregación, comunicación.
* Casos de uso y aplicaciones del Aprendizaje Federado (ej. dispositivos móviles, salud, sistemas de recomendación).
* Desafíos y limitaciones del Aprendizaje Federado (heterogeneidad de datos, comunicación, seguridad).
* Introducción a frameworks (ej. TensorFlow Federated, PySyft - a alto nivel conceptual).

Contenido Práctico:

* Ejemplo de un notebook de Python que simule el entrenamiento en varios "clientes" y la agregación de los modelos en un "servidor" central.
* Análisis de los resultados y discusión de cómo este enfoque protege la privacidad.

### [Clase 7 - Seguridad en IA y Gobernanza de Modelos](clase7/README.md) 

Contenido Teórico:

* Amenazas de seguridad específicas en sistemas de IA:
* Ataques de envenenamiento de datos (data poisoning): Manipulación de datos de entrenamiento.
* Ataques adversarios (adversarial attacks): Evasión, inversión de modelos, extracción de modelos.
* Fugas de privacidad: Exposición de información sensible a través del modelo.
* Estrategias de defensa y mitigación: adversarial training, differential privacy (introducción), model interpretability (XAI) como medida de confianza.
* Seguridad en la infraestructura MLOps: autenticación, autorización, gestión de secretos, aislamiento de recursos.
* Gobernanza de Modelos: ética en IA, cumplimiento normativo, auditabilidad, explicabilidad (XAI).

Contenido Práctico:

* Implementación de un mecanismo de seguridad básico en la API de FastAPI (ej. autenticación con API Key o JWT simple).
* Demostración de un ataque adversario simple y una discusión sobre posibles mitigaciones.
* Análisis de un caso de estudio real sobre un incidente de seguridad en IA y las lecciones aprendidas.

### [Sesión de Práctica Integrada / Taller de Proyecto Final](clase8/README.md) 

Sesión dedicada exclusivamente al proyecto final. Presentación técnica y de diseño relacionadas con:

* Integración de Airflow, MLflow, FastAPI y MinIO.
* Configuración y orquestación con Docker Compose.
* Implementación de los requisitos de los niveles de evaluación (local vs. contenedores).
* Exploración de los componentes opcionales (streaming, GraphQL/gRPC, seguridad avanzada).
* Revisión de arquitecturas de proyecto en grupo y discusión de buenas prácticas de código y documentación.


## Bibliografia

- Designing Machine Learning Systems. An Iterative Process for Production-Ready Applications - Chip Huyen (Ed. O’Reilly)
- Machine Learning Engineering with Python: Manage the production life cycle of machine learning models using MLOps with practical examples - Andrew P. McMahon (Ed. Packt Publishing)
- Engineering MLOps: Rapidly build, test, and manage production-ready machine learning life cycles at scale - Emmanuel Raj (Ed. Packt Publishing)
- Introducing MLOps: How to Scale Machine Learning in the Enterprise - Mark Treveil, Nicolas Omont, Clément Stenac, Kenji Lefevre, Du Phan, Joachim Zentici, Adrien Lavoillotte, Makoto Miyazaki, Lynn Heidmann (Ed. O’Reilly)
- Practical MLOps: Operationalizing Machine Learning Models - Noah Gift, Alfredo Deza (Ed. O’Reilly)
- Machine Learning Engineering - Andriy Burkov (Ed. True Positive Inc.)
- Machine Learning Engineering in Action - Ben Wilson (Manning)

---
Esta obra está bajo una
[Licencia Creative Commons Atribución-NoComercial-CompartirIgual 4.0 Internacional][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
