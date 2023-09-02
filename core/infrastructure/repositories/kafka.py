from kafka import KafkaProducer
from settings import KAFKA_SERVER


class KafkaProducerRepo:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=KAFKA_SERVER
        )

    def publish(self, topic, message):
        self.producer.send(topic, value=message)
        self.producer.flush()
        #self.producer.close()

