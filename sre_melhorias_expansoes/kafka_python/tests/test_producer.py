import unittest
from unittest.mock import patch, MagicMock
from producer.producer import KafkaProducerWrapper

class TestKafkaProducer(unittest.TestCase):

    @patch('producer.producer.KafkaProducer')
    def test_send_message_success(self, MockKafkaProducer):
        mock_producer = MockKafkaProducer.return_value
        producer = KafkaProducerWrapper(bootstrap_servers='localhost:9092', topic='test_topic')
        producer.send_message({'key': 'value'})
        mock_producer.send.assert_called_once_with('test_topic', value={'key': 'value'})
        mock_producer.flush.assert_called_once()

    @patch('producer.producer.KafkaProducer')
    def test_send_message_retry_on_failure(self, MockKafkaProducer):
        mock_producer = MockKafkaProducer.return_value
        mock_producer.send.side_effect = Exception("Test Exception")
        
        producer = KafkaProducerWrapper(bootstrap_servers='localhost:9092', topic='test_topic')
        with self.assertLogs(level='ERROR'):
            producer.send_message({'key': 'value'}, retries=2, retry_delay=1)

        self.assertEqual(mock_producer.send.call_count, 2)

