from entidades.vacina import Vacina
from telas.tela_vacina import TelaVacina


class ControladorVacinas():
    def __init__(self, controlador_sistema):
        self.__tela_vacina = TelaVacina()
        self.__controlador_sistema = controlador_sistema

    def incluir_vacina(self):
        while True:
            num_vacina = self.__tela_vacina.pega_nome_vacina()
            if num_vacina not in [1, 2, 3]:
                self.__tela_vacina.mostrar_mensagem(
                    "ERRO: Digite um valor válido.")
            else:
                if num_vacina == 1:
                    nome_vacina = Vacina('Raiva')
                elif num_vacina == 2:
                    nome_vacina = Vacina('Leptospirose')
                else:
                    nome_vacina = Vacina('Hepatite Infecciosa')
                return nome_vacina
