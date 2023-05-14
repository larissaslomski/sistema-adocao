from entidades.tipo_habitacao import TipoHabitacao
from telas.tela_tipo_habitacao import TelaTipoHabitacao


class ControladorTipoHabitacao:
    def __init__(self, controlador_sistema):
        self.__tela_tipo_habitacao = TelaTipoHabitacao()
        self.__controlador_sistema = controlador_sistema

    def incluir_tipo_habitacao(self):
        tipo_habitacao = self.abre_tela()
        self.__tela_tipo_habitacao.mostrar_mensagem(tipo_habitacao)
        return tipo_habitacao

    def cria_casa_pequena(self):
        tipo_habitacao = ['casa', 'pequena']
        return tipo_habitacao

    def cria_casa_media(self):
        tipo_habitacao = TipoHabitacao('casa', 'media')
        return tipo_habitacao

    def cria_casa_grande(self):
        tipo_habitacao = TipoHabitacao('casa', 'grande')
        return tipo_habitacao

    def cria_apartamento_pequeno(self):
        tipo_habitacao = TipoHabitacao('apartamento', 'pequeno')
        return tipo_habitacao

    def cria_apartamento_medio(self):
        tipo_habitacao = TipoHabitacao('apartamento', 'medio')
        return tipo_habitacao

    def cria_apartamento_grande(self):
        tipo_habitacao = TipoHabitacao('apartamento', 'grande')
        return tipo_habitacao

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cria_casa_pequena, 2: self.cria_casa_media, 3: self.cria_casa_grande, 4: self.cria_apartamento_pequeno,
                        5: self.cria_apartamento_medio, 6: self.cria_apartamento_grande, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_tipo_habitacao.tela_opcoes()]()
            break
