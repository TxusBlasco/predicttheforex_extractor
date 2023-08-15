import time
from settings import FREQUENCY


class ExtractorDomainService:
    def streamer(self, jobs: list):
        """
        Performs each action in the list [actions] with a frequency
        determined by the float FREQUENCY in seconds
        :param jobs: a list of actions to be performed
        :return: None
        """
        while True:
            [job() for job in jobs]
            time.sleep(FREQUENCY)

    def set_endpoint(self, broker, inst):
        endpoint = broker().set_endpoint(inst)
        return endpoint

    def clean_response(self, broker, response):
        clean = broker().clean_response(response)
        return clean

