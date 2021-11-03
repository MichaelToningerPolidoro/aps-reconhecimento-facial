class DadosNivelUm:
    _nomeProdutora = None
    _endereco = None
    _produtos = None
    _producao = None
    _destino = None
    _qtdEmpregados = None
    _qtdMaquinas = None
    _nivelAutomacao = None
    
    def __init__(self, dados):
        self._nomeProdutora = dados[0]
        self._endereco = dados[1]
        self._produtos = dados[2]
        self._producao = dados[3]
        self._destino = dados[4]
        self._qtdEmpregados = dados[5]
        self._qtdMaquinas = dados[6]
        self._nivelAutomacao = dados[7]

    def getNomeProdutora(self):
        return self._nomeProdutora

    def getEndereco(self):
        return self._endereco

    def getProdutos(self):
        return self._produdutos
    
    def getProducao(self):
        return self._producao

    def getDestino(self):
        return self._destino

    def getQuantiaEmpregados(self):
        return self._qtdEmpregados

    def getQuantidaMaquinas(self):
        return self._qtdMaquinas

    def getNivelAutomacao(self):
        return self._nivelAutomacao
