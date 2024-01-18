import core.domain.services.broker as broker_is
from core.domain.services.extractor import ExtractorDomainService as Ex
from core.infrastructure.repositories.kafka import KafkaProducerRepo as kfk
from core.infrastructure.repositories.source import BrokerRepo
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
        :return: a list of http responses from the broker, corresponding to
        each instrument to be retrieved.
        :return: a dictionary with broker response. Example: consider that self.insts = ['EUR_USD', 'EUR_JPY'], then
        clean will be:
        {
          "EUR_USD": {
            "complete": true,
            "volume": 2,
            "time": "2024-01-18T05:50:55.000000000Z",
            "bid": {
              "o": "1.08941",
              "h": "1.08941",
              "l": "1.08940",
              "c": "1.08940"
            },
            "mid": {
              "o": "1.08948",
              "h": "1.08948",
              "l": "1.08947",
              "c": "1.08947"
            },
            "ask": {
              "o": "1.08955",
              "h": "1.08955",
              "l": "1.08954",
              "c": "1.08954"
            }
          },
          "EUR_JPY": {
            "complete": true,
            "volume": 3,
            "time": "2024-01-18T05:50:55.000000000Z",
            "bid": {
              "o": "161.200",
              "h": "161.203",
              "l": "161.200",
              "c": "161.203"
            },
            "mid": {
              "o": "161.208",
              "h": "161.212",
              "l": "161.208",
              "c": "161.212"
            },
            "ask": {
              "o": "161.217",
              "h": "161.222",
              "l": "161.217",
              "c": "161.222"
            }
          }
        }
        """
        e = Ex()
        endpoints = self.set_endpoints()
        responses = {
            inst: BrokerRepo(endpoints[inst]).get_last_candle() for inst in endpoints
        }
        clean = {
            inst: e.clean(self.broker, responses[inst]) for inst in responses
        }
        print('\n')
        print(json.dumps(clean, indent=2))
        print('###############################################################')
        return clean

    def publish_candles(self):
        """
        Publishes one kafka message per each of the topic streams "inst" inside the list of instruments "insts",
        for example, if self.insts = ['EUR_USD', 'EUR_JPY'], then kafka will publish the parsed string of the
        following dictionary in kafka topic 'EUR_USD':
            {
                "complete": true,
                "volume": 2,
                "time": "2024-01-18T05:50:55.000000000Z",
                "bid": {
                  "o": "1.08941",
                  "h": "1.08941",
                  "l": "1.08940",
                  "c": "1.08940"
                },
                "mid": {
                  "o": "1.08948",
                  "h": "1.08948",
                  "l": "1.08947",
                  "c": "1.08947"
                },
                "ask": {
                  "o": "1.08955",
                  "h": "1.08955",
                  "l": "1.08954",
                  "c": "1.08954"
                }
              }
        and in the topic 'EUR_JPY', the following:
            {
                "complete": true,
                "volume": 3,
                "time": "2024-01-18T05:50:55.000000000Z",
                "bid": {
                  "o": "161.200",
                  "h": "161.203",
                  "l": "161.200",
                  "c": "161.203"
                },
                "mid": {
                  "o": "161.208",
                  "h": "161.212",
                  "l": "161.208",
                  "c": "161.212"
                },
                "ask": {
                  "o": "161.217",
                  "h": "161.222",
                  "l": "161.217",
                  "c": "161.222"
                }
              }

        :return: None
        """
        candles = self.get_last_candles()

        def bytify(message):
            """
            Encode the message to utf-8
            :param message:
            :return: the encoded message
            """
            return json.dumps(message, indent=2).encode('utf-8')

        [kfk().publish(inst, bytify(candles[inst])) for inst in candles]

    def fetch_stream(self):
        """
        Publishes one candle per topic to the streamer.
        :return:
        """
        jobs = [self.publish_candles]
        Ex().streamer(jobs)


# testing purpose:
if __name__ == '__main__':
    ExtractorAppService(insts=['EUR_USD', 'EUR_JPY']).fetch_stream()
