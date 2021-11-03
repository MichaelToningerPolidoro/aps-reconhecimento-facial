class DadosNivelTres:

    _descricaoAgrotoxico = None
    
    def __init__(self, dados):
        self._descricaoAgrotoxico = dados[0]

    def getDescricaoAgrotoxico(self):
        return self._descricaoAgrotoxico
