from settings import BROKER_ENVIRONMENT, PRICE, GRANULARITY


class IncoherentBrokerResponse(BaseException):
    pass


class Oanda:
    @staticmethod
    def set_endpoint(inst) -> str:
        """
        Builds the endpoint to get the last candle in Oanda broker
        :param env: oanda environment url. can be testing or real FX
        :param inst: instrument to be retrieved
        :param price: price type. Only admitted values: ask or bid
        :param gran: granularity
        :return: the url to be requested in the endpoint
        """
        url = [
            BROKER_ENVIRONMENT,
            r'/v3/instruments/',
            inst,
            r'/candles?price=',
            PRICE,
            r'&granularity=',
            GRANULARITY,
            r'&count=2'
            ]
        return ''.join(url)

    @staticmethod
    def clean(response) -> dict:
        if 'candles' in response:
            if response['candles'][-1]['complete']:
                return response['candles'][-1]
            elif not response['candles'][-1]['complete']:
                return response['candles'][-2]
        else:
            print('[ERROR] Incoherent broker response')
            return {}


# Add your additional broker here:
class AdditionalBroker:  # update the broker class name with your broker
    @staticmethod
    def set_endpoint(inst) -> str:
        # add here the code to build an endpoint
        return ''  # update the return

    @staticmethod
    def clean(response):
        # add here the code to post process the response from the broker
        return '' # update the return
