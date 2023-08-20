from kafka import KafkaConsumer
from core.infrastructure.repositories.kafka import KafkaProducerRepo


class TKafkaProducerRepo:
    def test_publish(self):
        KPR = KafkaProducerRepo()
        """for i in range(3):
            KPR.publish('EUR_USD', 'message_{}'.format(i))"""
        KPR.publish('test-topic', 'Hello, world')
        consumer = KafkaConsumer('test-topic')
        for msg in consumer:
            print(msg)
        consumer.close()

TKafkaProducerRepo().test_publish()