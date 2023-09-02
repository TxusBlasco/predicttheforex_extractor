import json
import requests
from helper.file_ops import Yaml
from settings import BROKER, SECRETS_PATH


class BrokerRepo:
    def __init__(self, endpoint: str):
        self.TOKEN = Yaml().read(SECRETS_PATH)[BROKER]['token']
        self.URL = endpoint

    def get_last_candle(self):
        try:
            head = {'Authorization': 'Bearer {}'.format(self.TOKEN)}
            response = requests.get(self.URL, headers=head)
            js = json.loads(response.content)
            response.raise_for_status()
            """print("[INFO] ------------------------------------")
            print("[INFO] Last candle extracted: ")
            print("[INFO] time: ",
                  txuslib.get_close_time_from_candle(js))
            print("[INFO] price: ",
                  txuslib.get_close_price_from_candle(js))
            print("[INFO] Status code: {}".format(
                response.status_code))
            print("[INFO] ------------------------------------")"""
            return js
        except requests.exceptions.HTTPError as e:
            return "[ERROR] Error: " + str(e)