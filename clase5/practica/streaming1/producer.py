import time
import json
import random
from kafka import KafkaProducer

def serialize_json(obj):
    return json.dumps(obj).encode('utf-8')

# Configuración del productor Kafka
producer = KafkaProducer(
    bootstrap_servers=['localhost:9094'], # Usar el puerto expuesto por Docker Compose
    value_serializer=serialize_json
)

topic_name = 'sensor_data'

print(f"Enviando datos al tópico: {topic_name}")

try:
    for i in range(100):
        sensor_id = random.randint(1, 5)
        temperature = round(random.uniform(20.0, 30.0), 2)
        humidity = round(random.uniform(40.0, 60.0), 2)
        pressure = round(random.uniform(900.0, 1100.0), 2)

        data = {
            'sensor_id': sensor_id,
            'timestamp': time.time(),
            'temperature': temperature,
            'humidity': humidity,
            'pressure': pressure
        }

        producer.send(topic_name, value=data)
        print(f"Sent: {data}")
        time.sleep(1) # Enviar un evento cada segundo

except KeyboardInterrupt:
    print("Deteniendo productor...")
finally:
    producer.close()
    print("Productor cerrado.")