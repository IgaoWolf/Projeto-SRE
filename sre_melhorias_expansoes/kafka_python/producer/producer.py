from kafka import KafkaProducer
import json
import logging
import time

class KafkaProducerWrapper:
    def __init__(self, bootstrap_servers, topic):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        self.topic = topic

    def send_message(self, message, retries=3, retry_delay=5):
        attempts = 0
        while attempts < retries:
            try:
                self.producer.send(self.topic, value=message)
                self.producer.flush()
                logging.info(f"Message sent: {message}")
                break
            except Exception as e:
                attempts += 1
                logging.error(f"Failed to send message, attempt {attempts}/{retries}: {e}")
                if attempts < retries:
                    time.sleep(retry_delay)
                else:
                    logging.error(f"Max retries reached. Failed to send message: {message}")

    def close(self):
        logging.info("Closing producer connection.")
        self.producer.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    producer = KafkaProducerWrapper(bootstrap_servers='localhost:9092', topic='test_topic')

    # Mensagem de exemplo para envio
    message = {"key": "value", "message": "Hello, Kafka!"}
    
    producer.send_message(message)
    producer.close()

