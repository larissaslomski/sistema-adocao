from entidades.pessoa import Pessoa
from entidades.tipo_habitacao import TipoHabitacao

class Adotante(Pessoa):
    def __init__(self, cpf: str, nome: str, nascimento: str, endereco: str, tipo_habitacao: TipoHabitacao, tem_outros_animais: bool):
        super().__init__(cpf, nome, nascimento, endereco)
        if isinstance(tem_outros_animais, bool):
            self.__tem_outros_animais = tem_outros_animais
        self.__tipo_habitacao = tipo_habitacao

    @property
    def tem_outros_animais(self):
        return self.__tem_outros_animais

    @tem_outros_animais.setter
    def tem_outros_animais(self, tem_outros_animais):
        if isinstance(tem_outros_animais, bool):
            self.__tem_outros_animais = tem_outros_animais



