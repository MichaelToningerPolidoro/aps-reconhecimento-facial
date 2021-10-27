import configparser
import mysql.connector

config = configparser.RawConfigParser()

config.read('config.config')

#Adicionar o db=... nos parametros ali
db = mysql.connector.connect(
    host=config.get('database', 'url'),
    user=config.get('database', 'user'),
    passwd=config.get('database', 'password')
)

cursor = db.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS testepython')

db.close()
