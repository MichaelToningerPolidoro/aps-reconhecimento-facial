class Usuario:
    _id: int = None
    _nome: str = None
    _nivelAcesso: int = None

    def __init__(self, id: int, nome: str , nivelAcesso: int):
        self._id = id
        self._nome = nome
        self._nivelAcesso = nivelAcesso

    def getId(self):
        return self._id

    def getNome(self):
        return self._nome

    def getNivelAcesso(self):
        return self._nivelAcesso
