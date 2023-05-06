from entidades.pessoa import Pessoa
# from tipo_habitacao import TipoHabitacao


class Adotante(Pessoa):
    def __init__(self, cpf: str, nome: str, nascimento: str, endereco: str, tem_outros_animais: bool):
        super().__init__(cpf, nome, nascimento, endereco)
        # if isinstance(tem_outros_animais, bool):
        #     self.__tem_outros_animais = tem_outros_animais
        # self.__tipo_habitacao = TipoHabitacao(self, tipo_habitacao, tamanho_habitacao)
        pass
