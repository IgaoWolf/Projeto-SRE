from kafka import KafkaConsumer
import json
import logging

logging.basicConfig(level=logging.INFO)

def create_consumer(bootstrap_servers, topic):
    return KafkaConsumer(
        topic,
        bootstrap_servers=bootstrap_servers,
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda v: json.loads(v.decode('utf-8'))
    )

def consume_messages(consumer):
    try:
        for message in consumer:
            logging.info(f"Message received: {message.value}")
    except Exception as e:
        logging.error(f"Error consuming message: {e}")
        raise

if __name__ == "__main__":
    consumer = create_consumer(['localhost:9095'], 'teste-topic')  # Usando Nginx como ponto de acesso
    consume_messages(consumer)

