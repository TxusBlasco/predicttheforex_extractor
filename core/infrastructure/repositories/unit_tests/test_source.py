from core.infrastructure.repositories.source import BrokerRepo


class TestBrokerRepo:
    def test_get_last_candle(self):
        endpoint = 'https://api-fxpractice.oanda.com/v3/instruments/EUR_USD/candles?price=MAB&granularity=S5&count=2'
        to_be_tested = BrokerRepo(endpoint).get_last_candle()
        assert to_be_tested['instrument']
        assert to_be_tested['granularity']
        assert to_be_tested['candles']
