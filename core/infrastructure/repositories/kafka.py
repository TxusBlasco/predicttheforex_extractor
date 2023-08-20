from kafka import KafkaProducer
from settings import KAFKA_BROKER


class KafkaProducerRepo:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=KAFKA_BROKER,
            value_serializer=lambda x: x.encode("utf-8")
        )

    def publish(self, topic, message):
        self.producer.send(topic, value=message)
        self.producer.flush()
        #self.producer.close()
