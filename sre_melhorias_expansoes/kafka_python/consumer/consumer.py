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
    # Usando o IP do HAProxy
    consumer = create_consumer(['172.18.0.6:9095'], 'teste-topic')
    consume_messages(consumer)

