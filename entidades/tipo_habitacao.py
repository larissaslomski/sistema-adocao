
class TipoHabitacao:
    def __init__(self, tipo_habitacao: str, tamanho_habitacao: str):
        if isinstance(tipo_habitacao, str):
            self.__tipo_habitacao = tipo_habitacao
        if isinstance(tamanho_habitacao, str):
            self.__tamanho_habitacao = tamanho_habitacao


@property
def tipo_habitacao(self):
    return self.__tipo_habitacao

@property
def tamanho_habitacao(self):
    return self.__tamanho_habitacao

@tipo_habitacao.setter
def tipo_habitacao(self, tipo_habitacao):
    self.__tipo_habitacao = tipo_habitacao

@tamanho_habitacao.setter
def tamanho_habitacao(self, tamanho_habitacao):
    self.__tamanho_habitacao = tamanho_habitacao