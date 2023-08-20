import time
from settings import FREQUENCY


class ExtractorDomainService:
    def streamer(self, jobs: list, stop: bool = False):
        """
        Performs each action in the list [actions] with a frequency
        determined by the float FREQUENCY in seconds
        :param jobs: a list of actions to be performed
        :param stop: condition that makes the loop stop
        :return: a string 'STOP'
        """
        while True:
            if stop:
                break
            [job() for job in jobs]
            time.sleep(FREQUENCY)
        print('[INFO] Streamer has stopped')
        return 'STOP'

    def set_endpoint(self, broker, inst):
        endpoint = broker().set_endpoint(inst)
        return endpoint

    def clean(self, broker, response):
        clean = broker().clean(response)
        return clean

