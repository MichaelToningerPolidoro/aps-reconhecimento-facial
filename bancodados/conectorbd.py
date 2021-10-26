import configparser

config = configparser.RawConfigParser()

config.read('config.config')
print(config.get('database', 'url'))
print(config.get('database', 'user'))
print(config.get('database', 'password'))
