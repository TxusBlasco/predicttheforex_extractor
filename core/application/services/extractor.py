import core.domain.services.broker as broker_is
from core.domain.services.extractor import ExtractorDomainService as Ex
from core.infrastructure.repositories.kafka import KafkaProducerRepo as kfk
from core.infrastructure.repositories.source import BrokerRepo as Br
from settings import BROKER
import json


class ExtractorAppService:
    def __init__(self, insts: list[str]):
        self.insts = insts
        self.broker = self.get_broker()

    def get_broker(self):
        match BROKER:
            case 'Oanda':
                return broker_is.Oanda

            # 'Add a broker here'
            # case 'Additional_broker':
            #   return broker_is.AdditionalBroker

    def set_endpoints(self) -> dict:
        """
        Build a dictionary of instrument keys and endpoints to be called
        :return: a dictionary of keys and endpoints:
            {
                'inst_1': 'endpoint 1',
                ...
                'inst_n': 'endpoint_n'
            }
        """
        e = Ex()
        endpoints = {
            inst: e.set_endpoint(self.broker, inst) for inst in self.insts
        }
        return endpoints

    def get_last_candles(self) -> dict:
        """
        Get the last price data in form of dictionaries from the broker
        :return: a list of http responses from the broker, correspondoing to
        each instrument to be retrieved
        """
        e = Ex()
        endpoints = self.set_endpoints()
        responses = {
            inst: Br(endpoints[inst]).get_last_candle() for inst in endpoints
        }
        clean = {
            inst: e.clean(self.broker, responses[inst]) for inst in responses
        }
        print('\n')
        print(json.dumps(clean, indent=2))
        print('###############################################################')
        return clean

    def publish_candles(self):
        candles = self.get_last_candles()

        def bytify(message):
            return json.dumps(message, indent=2).encode('utf-8')

        [kfk().publish(inst, bytify(candles[inst])) for inst in candles]

    def fetch_stream(self):
        jobs = [self.publish_candles]
        Ex().streamer(jobs)


# testing purpose:
if __name__ == '__main__':
    ExtractorAppService(insts=['EUR_USD', 'EUR_JPY']).fetch_stream()
