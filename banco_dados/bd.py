import configparser
import mysql.connector

config = configparser.RawConfigParser()
config.read('config.config')
bdurl = config.get('database', 'url')
bdusuario = config.get('database', 'user')
bdsenha = config.get('database', 'password')
bdnome = 'testepython'

def buscarNomePessoaReconhecida(idPessoaReconhecida: int) -> str:
    bd = mysql.connector.connect(host=bdurl, user=bdusuario, passwd=bdsenha, database=bdnome)
    cursor = bd.cursor()
    cursor.execute(f'SELECT nome FROM teste where id = {idPessoaReconhecida}')
    nome = cursor.fetchone()[0]
    bd.close()
    return nome
