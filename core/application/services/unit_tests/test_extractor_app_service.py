from core.application.services.extractor import ExtractorAppService
from core.domain.services.broker import Oanda

EAS = ExtractorAppService(broker='Oanda', insts=['EUR_USD'])


class TestExtractorAppService:
    def test_get_broker(self):
        assert issubclass(EAS.get_broker(), Oanda)

    def test_set_endpoints(self):
        endpoints = EAS.set_endpoints()
        assert 'EUR_USD' in endpoints
        assert 'https://' in endpoints['EUR_USD']
        assert 'instruments' in endpoints['EUR_USD']
        assert '/v3/instruments/EUR_USD/candles?price=' in endpoints['EUR_USD']
        assert '&granularity=' in endpoints['EUR_USD']
        assert '&count=2' in endpoints['EUR_USD']

    def test_get_last_candles(self):
        last_candles = EAS.get_last_candles()
        assert 'candles' not in last_candles
        assert last_candles['EUR_USD']['complete']
        assert 'time' in last_candles['EUR_USD']
        assert 'volume' in last_candles['EUR_USD']
