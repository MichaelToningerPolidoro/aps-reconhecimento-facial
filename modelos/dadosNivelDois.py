class DadosNivelDois:

    _incentivosFiscais = None
    _impostosMunicipais = None
    _impostosEstaduais = None
    _impostosFederais = None
    _taxasFederais = None
    
    def __init__(self, dados):
        self._incentivosFiscais = dados[0]
        self._impostosMunicipais = dados[1]
        self._impostosEstaduais = dados[2]
        self._impostosFederais = dados[3]
        self._taxasFederais = dados[4]

    def getIncentivosFiscais(self):
        return self._incentivosFiscais

    def getImpostosMunicipais(self):
        return self._impostosMunicipais

    def getImpostosEstaduais(self):
        return self._impostosEstaduais

    def getImpostosFederais(self):
        return self._impostosFederais
    
    def getTaxasFederais(self):
        return self._taxasFederais
