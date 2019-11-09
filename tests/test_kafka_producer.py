import unittest
from producer.event_broadcaster import Broadcaster


class TestKafkaProducer(unittest.TestCase):

    def setUp(self) -> None:
        kafka_producer = Broadcaster()
