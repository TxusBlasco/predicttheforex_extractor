import os

FREQUENCY = 0.1
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PRICE = 'MAB'
GRANULARITY = 'S5'
BROKER = 'Oanda'
TESTING_ENVIRONMENT = r'https://api-fxpractice.oanda.com'
TRADING_ENVIRONMENT = ''
BROKER_ENVIRONMENT = TESTING_ENVIRONMENT
SECRETS_PATH = r'C:\Users\Jesus Garcia\Google Drive\OANDA\secrets\secrets.yaml'
KAFKA_SERVER = 'localhost:9092'