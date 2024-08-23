from kafka import KafkaProducer
import json
import time
import logging

logging.basicConfig(level=logging.INFO)

def create_producer(bootstrap_servers):
    return KafkaProducer(
        bootstrap_servers=bootstrap_servers,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

def send_message(producer, topic, message):
    try:
        producer.send(topic, message)
        producer.flush()
        logging.info(f"Message sent: {message}")
    except Exception as e:
        logging.error(f"Error sending message: {e}")
        raise

def send_message_with_retries(producer, topic, message, retries=5, delay=2):
    attempt = 0
    while attempt < retries:
        try:
            send_message(producer, topic, message)
            return
        except KafkaError as e:
            logging.error(f"Retry {attempt + 1}/{retries}: Failed to send message. Error: {e}")
            attempt += 1
            time.sleep(delay)
    logging.error("Max retries reached. Message failed to send.")

if __name__ == "__main__":
    producer = create_producer(['kafka1:9092'])
    for i in range(10):
        send_message_with_retries(producer, 'teste-topic', {'key': f'message-{i}', 'value': i})
        time.sleep(1)

