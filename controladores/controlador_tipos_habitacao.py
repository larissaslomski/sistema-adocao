from entidades.tipo_habitacao import TipoHabitacao
from telas.tela_tipo_habitacao import TelaTipoHabitacao


class ControladorTipoHabitacao:
    def __init__(self, controlador_sistema):
        self.__tipos_habitacao = []
        self.__tela_tipo_habitacao = TelaTipoHabitacao()
        self.__controlador_sistema = controlador_sistema

    # O usuario seleciona os tipo_hab e tamanho_hab através da tela e ela retorna os valores para o controlador

    # Para alterar os atributos de tipo_habitacao
    # O identificador do tipo de habitacao pode ser o cpf relacionado, ou seja, o cpf também seria atributo de 
    # tipo_habitacao, ja que o controlador de tipos_habitacao não conhece a classe adotante
     
    def casa_pequena(self):
        tipo_habitacao = TipoHabitacao('casa', 'pequena')
        self.__habitacoes.append(tipo_habitacao)

    def casa_media(self):
        tipo_habitacao = TipoHabitacao('casa', 'media')
        self.__habitacoes.append(tipo_habitacao)

    def casa_grande(self):
        tipo_habitacao = TipoHabitacao('casa', 'grande')
        self.__habitacoes.append(tipo_habitacao)

    def apartamento_pequeno(self):
        tipo_habitacao = TipoHabitacao('apartamento', 'pequeno')
        self.__habitacoes.append(tipo_habitacao)

    def apartamento_medio(self):
        tipo_habitacao = TipoHabitacao('apartamento', 'medio')
        self.__habitacoes.append(tipo_habitacao)

    def apartamento_grande(self):
        tipo_habitacao = TipoHabitacao('apartamento', 'grande')
        self.__habitacoes.append(tipo_habitacao)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.casa_pequena, 2: self.casa_media, 3: self.casa_grande, 4: self.apartamento_pequeno,
                        5: self.apartamento_medio, 6: self.apartamento_grande, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_tipo_habitacao.tela_opcoes()]()
