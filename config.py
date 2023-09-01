from configparser import ConfigParser


config = ConfigParser()
config.read('config.ini')

config_db = config['db']

MYSQL_HOST = config_db['host']
MYSQL_PORT = int(config_db['port'])
MYSQL_USER = config_db['user']
MYSQL_PASSWORD = config_db['password']
MYSQL_NAME = config_db['name']
