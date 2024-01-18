import time
from settings import LISTENER_FREQ


class ExtractorDomainService:
    @staticmethod
    def streamer(jobs: list, stop: bool = False):
        """
        Performs each action in the list [jobs] with a frequency determined by the float FREQUENCY in seconds. For
        example, it can get prices every 0.1 seconds. Streamer can work as a listener, but it does not know
        when the broker is going to publish a new candle. So it has to continuously ask for a new candle
        :param jobs: a list of actions to be performed. If one of the actions returns stop = True, the stream stops
        :param stop: condition that makes the loop stop
        :return: a string 'STOP'
        """
        while True:
            if stop:
                break
            [job() for job in jobs]
            time.sleep(LISTENER_FREQ)
        print('[INFO] Streamer has stopped')
        return 'STOP'

    @staticmethod
    def set_endpoint(broker, inst):
        endpoint = broker().set_endpoint(inst)
        return endpoint

    @staticmethod
    def clean(broker, response):
        clean = broker().clean(response)
        return clean

