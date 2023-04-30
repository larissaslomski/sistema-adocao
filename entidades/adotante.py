from pessoa import Pessoa
from tipo_habitacao import TipoHabitacao


class Adotante(Pessoa):
    def __init__(self, cpf: str, nome: str, nascimento: str, endereco: str, tipo_habitacao: TipoHabitacao,
                 tem_outros_animais: bool):
        super().__init__(cpf, nome, nascimento, endereco)
        if isinstance(tipo_habitacao, TipoHabitacao) and isinstance(tem_outros_animais, bool):
            self.__tipo_habitacao = tipo_habitacao
            self.__tem_outros_animais = tem_outros_animais


