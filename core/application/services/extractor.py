import core.domain.services.broker as broker_is
from core.domain.services.extractor import ExtractorDomainService as Ex
from core.infrastructure.repositories.source import BrokerRepo as Br


class ExtractorAppService:
    def __init__(self, broker, insts: list[str],):
        self.broker = broker
        self.insts = insts

    def get_broker(self):
        match self.broker:
            case 'Oanda':
                return broker_is.Oanda

    def set_endpoints(self) -> list[str]:
        """
        Build a list of endpoint urls corresponding to each one of the
        instruments to be retrieved
        :return: a list of endpoint urls
        """
        e = Ex()
        broker = self.get_broker
        endpoints = [e.set_endpoint(broker, inst) for inst in self.insts]
        return endpoints

    def get_last_candles(self) -> list[dict]:
        """
        Get the last price data in form of dictionaries from the broker
        :return: a list of http responses from the broker, correspondoing to
        each instrument to be retrieved
        """
        e = Ex()
        broker = self.get_broker
        endpoints = self.set_endpoints()
        responses = [Br(endpoint).get_last_candle() for endpoint in endpoints]
        clean = [e.clean_response(broker, resp) for resp in responses]
        return clean

    def publish_partition(self, candles):
        pass

    def publish_candles(self):
        candles = self.get_last_candles()
        self.publish_partition(candles)


    def fetch_stream(self):
        jobs = [self.publish_candles()]
        Ex().streamer(jobs)

    def get_bulk_price(self, start: str, end: str):
        pass
