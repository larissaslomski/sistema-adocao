from entidades.pessoa import Pessoa
from controladores.controlador_tipos_habitacao import ControladorTipoHabitacao


class Adotante(Pessoa):
    def __init__(self, cpf: str, nome: str, nascimento: str, endereco: str, tem_outros_animais: bool):
        super().__init__(cpf, nome, nascimento, endereco)
        if isinstance(tem_outros_animais, bool):
            self.__tem_outros_animais = tem_outros_animais
        self.__tipo_habitacao = ControladorTipoHabitacao.abre_tela(self)

