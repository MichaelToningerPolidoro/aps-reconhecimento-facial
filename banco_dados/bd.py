import configparser
import mysql.connector

class Bd:
    _bdurl: str = None
    _bdusuario: str = None
    _bdsenha: str = None
    _bdnome: str = None
    _conexaoBd = None

    def __init__(self):
        config = configparser.RawConfigParser()
        config.read('config.config')
        self._bdurl = config.get('database', 'url')
        self._bdusuario = config.get('database', 'user')
        self._bdsenha = config.get('database', 'password')
        self._bdnome = config.get('database', 'dbname')

    def conectarBd(self):
        self._conexaoBd = mysql.connector.connect(
            host=self._bdurl, user=self._bdusuario, passwd=self._bdsenha, database=self._bdnome
        )

        return self._conexaoBd.cursor()

    def executarQuery(self, query: str):
        cursor = self.conectarBd()
        cursor.execute(query)
        resultado = cursor.fetchone()
        self._conexaoBd.close()
        return resultado

    def obterDadosPessoaReconhecida(self, idPessoaReconhecida: int):
        return self.executarQuery(f'SELECT Nome, NivelAcesso FROM Usuario WHERE Id={idPessoaReconhecida};')

    def obterDadosNivelUm(self, idProdutora: int):
        return self.executarQuery(f"""
            SELECT 
                Nome, Endereco, Produtos, ProducaoAnual, DestinoProducao, QtdEmpregados, QtdMaquinas, NivelAutomacao 
            FROM 
                Produtora
            WHERE
                Id = {idProdutora}
        """)

    def obterDadosNivelDois(self, idProdutora: int):
        return self.executarQuery(f"""
            SELECT
                IncentivosFiscais, ImpostosMunicipais, ImpostosEstadual, ImpostosFederal, TaxasFederal
            FROM
                Impostos
            WHERE
                Id = {idProdutora}
        """)

    def obterDadosNivelTres(self, idProdutora: int):
        return self.executarQuery(f"""
            SELECT
                Descricao
            FROM
                Agrotoxico
            WHERE
                Id = {idProdutora}
        """)
