class Usuario:
    _nome = None
    _nivelAcesso = None

    def __init__(self, nome: str , nivelAcesso: int):
        self._nome = nome
        self._nivelAcesso = nivelAcesso

    def getNome(self):
        return self._nome

    def getNivelAcesso(self):
        return self._nivelAcesso
