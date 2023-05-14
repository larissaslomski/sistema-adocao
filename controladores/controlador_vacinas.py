from entidades.vacina import Vacina
from telas.tela_vacina import TelaVacina


class ControladorVacinas():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__vacinas = []
        self.__tela_vacina = TelaVacina()

    def pega_vacina_por_nome(self, nome: str):
        for vacina in self.__vacinas:
            if (vacina.nome_vacina == nome):
                return vacina
        return None

    def incluir_vacina(self):
        dados_vacina = self.__tela_vacina.pega_vacina_nome()
        if dados_vacina is not None:
            vacina = Vacina(dados_vacina["nome_vacina"])
            self.__vacinas.append(vacina)
            self.__tela_vacina.mostra_mensagem("Vacina cadastrada com sucesso no sistema.")
        # else:
        #     self.__tela_vacina.mostra_mensagem("ERRO: o Animal ja esta cadastrado no Sistema.")

    def listar_vacina(self):
        tam_lista_vacina = len(self.__vacinas)
        if tam_lista_vacina > 0:
            for vacina in self.__vacinas:
                self.__tela_vacina.mostra_vacina(
                    {"nome_vacina": vacina.nome_vacina})
        else:
            self.__tela_vacina.mostra_mensagem(
                "ERRO: Não existe nenhuma vacina cadastrada no sistema.")
            self.__controlador_sistema.abre_tela()

    def alterar_vacina(self):
        self.listar_vacina()
        nome_vacina = self.__tela_vacina.pega_vacina_nome()
        vacina = self.pega_vacina_por_nome(nome_vacina)

        if (vacina is not None):
            novos_dados_vacina = self.__tela_vacina.pega_vacina_nome()
            vacina.nome = novos_dados_vacina["nome_vacina"]
            self.listar_vacina()
        else:
            self.__tela_vacina.mostra_mensagem(
                "ERRO: A vacina não existe.")
            self.__tela_vacina.tela_opcoes()

    def excluir_vacina(self):
        self.listar_vacina()
        nome_vacina = self.__tela_vacina.seleciona_vacina()
        vacina = self.pega_vacina_por_nome(nome_vacina)

        if vacina is not None:
            self.__vacinas.remove(vacina)
            self.__tela_vacina.mostra_mensagem(f"A vacina: {nome_vacina} foi excluida do sistema")
            if len(self.__vacinas) == 0:
                self.__tela_vacina.mostra_mensagem("Não existe nenhuma vacina cadastrada no sistema")
            else:
                self.__tela_vacina.tela_opcoes()
        else:
            self.__tela_vacina.mostra_mensagem("ERRO: A vacina não existe.")
            self.__tela_vacina.tela_opcoes()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_vacina(), 2: self.alterar_vacina(),
                        3: self.listar_vacina(), 4: self.excluir_vacina(), 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_vacina.tela_opcoes()]()

