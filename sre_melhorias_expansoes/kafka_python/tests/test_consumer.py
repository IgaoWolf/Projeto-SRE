import unittest
from unittest.mock import patch, MagicMock
from consumer.consumer import KafkaConsumerWrapper

class TestKafkaConsumer(unittest.TestCase):

    @patch('consumer.consumer.KafkaConsumer')
    def test_consume_messages(self, MockKafkaConsumer):
        mock_consumer = MockKafkaConsumer.return_value
        mock_consumer.__iter__.return_value = [{'key': 'value'}]

        consumer = KafkaConsumerWrapper(bootstrap_servers='localhost:9092', topic='test_topic', group_id='test_group')
        with self.assertLogs(level='INFO'):
            consumer.consume_messages()

        mock_consumer.__iter__.assert_called_once()

if __name__ == '__main__':
    unittest.main()

