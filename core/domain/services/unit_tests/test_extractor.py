from core.domain.services.extractor import ExtractorDomainService
from core.domain.services.broker import Oanda


class TestExtractorDomainService:
    def test_set_endpoint(self):
        # If this test fails, consider verifying price and granularity in
        # settings.py
        ground_truth = 'https://api-fxpractice.oanda.com/v3/instruments/' \
                       'EUR_USD/candles?price=MAB&granularity=S5&count=2'
        EDS = ExtractorDomainService()
        to_be_tested = EDS.set_endpoint(Oanda, 'EUR_USD')
        assert ground_truth == to_be_tested

    def test_clean(self):
        EDS = ExtractorDomainService()

        response_last_false = {
            "candles": [
                {
                    "complete": True,
                    "mid": {
                        "c": "1.09954",
                        "h": "1.09954",
                        "l": "1.09954",
                        "o": "1.09951"
                    },
                    "time": "2016-10-17T15:17:15.000000000Z",
                    "volume": 1
                },
                {
                    "complete": False,
                    "mid": {
                        "c": "1.09961",
                        "h": "1.09961",
                        "l": "1.09958",
                        "o": "1.09954"
                    },
                    "time": "2016-10-17T15:17:20.000000000Z",
                    "volume": 3
                }
            ],
            "granularity": "S5",
            "instrument": "EUR/USD"
        }

        false_to_be_tested = EDS.clean(Oanda, response_last_false)
        ground_truth_false = {
            "complete": True,
            "mid": {
                "c": "1.09954",
                "h": "1.09954",
                "l": "1.09954",
                "o": "1.09951"
            },
            "time": "2016-10-17T15:17:15.000000000Z",
            "volume": 1
        }
        assert false_to_be_tested == ground_truth_false

        response_last_true = {
            "candles": [
                {
                    "complete": True,
                    "mid": {
                        "c": "1.09954",
                        "h": "1.09954",
                        "l": "1.09954",
                        "o": "1.09951"
                    },
                    "time": "2016-10-17T15:17:15.000000000Z",
                    "volume": 1
                },
                {
                    "complete": True,
                    "mid": {
                        "c": "1.09961",
                        "h": "1.09961",
                        "l": "1.09958",
                        "o": "1.09954"
                    },
                    "time": "2016-10-17T15:17:20.000000000Z",
                    "volume": 3
                }
            ],
            "granularity": "S5",
            "instrument": "EUR/USD"
        }

        true_to_be_tested = EDS.clean(Oanda, response_last_true)
        ground_truth_true = {
            "complete": True,
            "mid": {
                "c": "1.09961",
                "h": "1.09961",
                "l": "1.09958",
                "o": "1.09954"
            },
            "time": "2016-10-17T15:17:20.000000000Z",
            "volume": 3
        }
        assert true_to_be_tested == ground_truth_true

        incoherent_response = {'No candles to be shown'}
        incoherent_to_be_tested = EDS.clean(Oanda, incoherent_response)
        assert incoherent_to_be_tested == {}