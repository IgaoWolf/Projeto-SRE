from kafka import KafkaConsumer
import json
import logging

class KafkaConsumerWrapper:
    def __init__(self, bootstrap_servers, topic, group_id):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id=group_id,
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )

    def consume_messages(self):
        try:
            logging.info(f"Consumer is now listening to topic: {self.consumer.topics()}")

            for message in self.consumer:
                logging.info(f"Consumed message: {message.value}")
                # Aqui você pode adicionar qualquer processamento que deseje fazer com a mensagem
                print(f"Received message: {message.value}")
                
        except Exception as e:
            logging.error(f"Error consuming messages: {e}")
        finally:
            self.close()

    def close(self):
        logging.info("Closing consumer connection.")
        self.consumer.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    consumer = KafkaConsumerWrapper(bootstrap_servers='localhost:9092', topic='test_topic', group_id='test_group')
    consumer.consume_messages()

