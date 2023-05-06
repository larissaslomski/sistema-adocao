from entidades.pessoa import Pessoa


class Doador(Pessoa):
    def __init__(self, cpf: str, nome: str, nascimento: str, endereco: str):
        super().__init__(cpf, nome, nascimento, endereco)

