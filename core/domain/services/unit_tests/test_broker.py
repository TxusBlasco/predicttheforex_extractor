from core.domain.services.broker import Oanda


class TestOanda:
    def test_set_endpoint(self):
        # If this test fails, consider verifying price and granularity in
        # settings.py
        ground_truth = 'https://api-fxpractice.oanda.com/v3/instruments/' \
                       'EUR_USD/candles?price=MAB&granularity=S5&count=2'
        to_be_tested = Oanda().set_endpoint('EUR_USD')
        assert ground_truth == to_be_tested