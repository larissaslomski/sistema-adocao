from entidades.vacina import Vacina
from telas.tela_vacina import TelaVacina


class ControladorVacinas():
    def __init__(self):
        self.__tela_vacina = TelaVacina()

    def incluir_vacina(self):
        while True:
            dados_vacina = self.__tela_vacina.pega_nome_vacina()
            if dados_vacina not in [1, 2, 3]:
                self.__tela_vacina.mostrar_mensagem(
                    "ERRO: Digite um valor válido.")
            else:
                if tipo_habitacao == 1:
                    tipo_habitacao = Vacina('Raiva')
                elif tipo_habitacao == 2:
                    tipo_habitacao = Vacina('Leptospirose')
                else:
                    tipo_habitacao = Vacina('Hepatite Infecciosa')
                return tipo_habitacao
