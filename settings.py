import os

LISTENER_FREQ = 0.01
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PRICE = 'MAB'
GRANULARITY = 'S5'
BROKER = 'Oanda'
TESTING_ENVIRONMENT = r'https://api-fxpractice.oanda.com'
TRADING_ENVIRONMENT = ''
BROKER_ENVIRONMENT = TESTING_ENVIRONMENT
KAFKA_SERVER = 'localhost:9092'
SECRETS_PATH = r'C:\Users\Txus Blasco\Desktop\OANDA\secrets\secrets.yaml'