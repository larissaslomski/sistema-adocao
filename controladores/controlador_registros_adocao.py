from entidades.registro_adocao import RegistroAdocao
from telas.tela_registro_adocao import TelaRegistroAdocao
from uuid import uuid4
from datetime import datetime
from datetime import date


class ControladorRegistrosAdocao():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__registros_adocao = []
        self.__tela_registro_adocao = TelaRegistroAdocao()

    def pega_registro_adocao_por_codigo(self, codigo: int):
        for registro_adocao in self.__registros_adocao:
            if registro_adocao.codigo_registro == codigo:
                return registro_adocao
        return None

    def verifica_se_nao_doou(self, adotante):
        if self.__controlador_sistema.controlador_registros_doacao.pega_registro_doacao_por_doador(adotante) is None:
            return True
        else:
            return False

    def verifica_vacinas(self, animal):
        quantidade_vacina = len(animal.historicos_vacinacao)
        if quantidade_vacina == 3:
            return True
        else:
            return False

    def verifica_maior_idade(self, data_nascimento):
        data_atual = datetime.now().date()
        idade_minima = 18
        try:
            data_formatada = datetime.strptime(
                data_nascimento, "%d/%m/%Y").date()
            diferenca_anos = data_atual.year - data_formatada.year
            if (data_atual.month, data_atual.day) < (data_formatada.month, data_formatada.day):
                diferenca_anos -= 1
            if diferenca_anos >= idade_minima:
                return True
            else:
                return False
        except ValueError:
            self.__tela_registro_adocao.mostra_mensagem(
                "Formato de data inválido. Utilize o formato dd/mm/aaaa.")

    def incluir_registro_adocao(self):
        cachorro_ou_gato = self.__tela_registro_adocao.seleciona_cachorro_ou_gato()
        while True:
            if cachorro_ou_gato not in (1, 2):
                self.__tela_registro_adocao.mostra_mensagem(
                    "Opção inválida! Selecione 1 ou 2!")
                cachorro_ou_gato = self.__tela_registro_adocao.seleciona_cachorro_ou_gato()
            else:
                break
        if cachorro_ou_gato == 1:
            self.__tela_registro_adocao.mostra_mensagem(
                "Precisamos do CPF do adotante e o número do chip do cachorro:")
            self.__controlador_sistema.controlador_cachorros.listar_cachorros()
            self.__controlador_sistema.controlador_adotantes.listar_adotantes()
            dados_registro_adocao = self.__tela_registro_adocao.pega_dados_registro_adocao()
            adotante = self.__controlador_sistema.controlador_adotantes.pega_adotante_por_cpf(
                dados_registro_adocao["cpf"])
            cachorro = self.__controlador_sistema.controlador_cachorros.pega_cachorro_por_num_chip(
                dados_registro_adocao["numero_chip"])
            if adotante is not None and cachorro is not None:
                maior_idade = self.verifica_maior_idade(
                    adotante.nascimento)
                tomou_vacinas = self.verifica_vacinas(cachorro)
                nao_doou = self.verifica_se_nao_doou(adotante)
                if maior_idade:
                    if tomou_vacinas:
                        if nao_doou:
                            codigo_registro = uuid4().int
                            data = date.today()
                            registro_adocao = RegistroAdocao(
                                codigo_registro, data, cachorro, adotante, False)
                            self.__registros_adocao.append(registro_adocao)
                            self.__tela_registro_adocao.mostra_mensagem(
                                f"Inclusão de registro de adoção realizada com sucesso")
                        else:
                            self.__tela_registro_adocao.mostra_mensagem(
                                f"O adotante já foi um doador")
                    else:
                        self.__tela_registro_adocao.mostra_mensagem(
                            f"ATENÇAO: O animal não tem as três vacinas necessárias.")
                        self.retornar()
                else:
                    self.__tela_registro_adocao.mostra_mensagem(
                        f"ATENÇAO: Somente maiores de idade podem adotar.")
                    self.retornar()
            else:
                self.__tela_registro_adocao.mostra_mensagem(
                    "Não há nenhum cachorro cadastrado disponível para adoção")
        elif cachorro_ou_gato == 2:
            self.__tela_registro_adocao.mostra_mensagem(
                "Precisamos do CPF do adotante e o número do chip do gato:")
            self.__controlador_sistema.controlador_gatos.listar_gatos()
            self.__controlador_sistema.controlador_adotantes.listar_adotantes()
            dados_registro_adocao = self.__tela_registro_adocao.pega_dados_registro_adocao()
            adotante = self.__controlador_sistema.controlador_adotantes.pega_adotante_por_cpf(
                dados_registro_adocao["cpf"])
            gato = self.__controlador_sistema.controlador_gatos.pega_gato_por_num_chip(
                dados_registro_adocao["numero_chip"])
            if adotante is not None and gato is not None:
                maior_idade = self.verifica_maior_idade(
                    adotante.nascimento)
                tomou_vacinas = self.verifica_vacinas(gato)
                nao_doou = self.verifica_se_nao_doou(adotante)
                if maior_idade:
                    if tomou_vacinas:
                        if nao_doou:
                            codigo_registro = uuid4().int
                            data = date.today()
                            registro_adocao = RegistroAdocao(
                                codigo_registro, data, gato, adotante, False)
                            self.__registros_adocao.append(registro_adocao)
                            self.__tela_registro_adocao.mostra_mensagem(
                                f"Inclusão de registro de adoção realizada com sucesso")
                        else:
                            self.__tela_registro_adocao.mostra_mensagem(
                                f"O adotante já foi um doador")
                    else:
                        self.__tela_registro_adocao.mostra_mensagem(
                            f"ATENÇAO: O animal não tem as três vacinas necessárias.")
                        self.retornar()
                else:
                    self.__tela_registro_adocao.mostra_mensagem(
                        f"ATENÇAO: Somente maiores de idade podem adotar.")
                    self.retornar()
            else:
                self.__tela_registro_adocao.mostra_mensagem(
                    "Não há nenhum gato cadastrado disponível para adoção")

    def listar_registro_adocao(self):
        for registro_adocao in self.__registros_adocao:
            # inserir animalfazer metodo abstrato em animal
            self.__tela_registro_adocao.mostra_registro_adocao({"codigo_registro": registro_adocao.codigo_registro,
                                                                "data": registro_adocao.data,
                                                                "cpf_adotante": registro_adocao.adotante.cpf,
                                                                "termo_responsabilidade": registro_adocao.termo_responsabilidade})

    def excluir_registro_adocao(self):
        self.listar_registro_adocao()
        codigo_registro_adocao = self.__tela_registro_adocao.seleciona_registro_adocao()
        registro_adocao = self.pega_registro_adocao_por_codigo(
            int(codigo_registro_adocao))

        if registro_adocao is not None:
            self.__registros_adocao.remove(registro_adocao)
            self.__tela_registro_adocao.mostra_mensagem(
                f"Registro de adoção com código {codigo_registro_adocao} removido com sucesso.")
            self.listar_registro_adocao()
        else:
            self.__tela_registro_adocao.mostra_mensagem(
                "ATENCAO: Codigo de registro não existente")

    def alterar_registro_adocao(self):
        pass

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_registro_adocao, 2: self.listar_registro_adocao, 3: self.excluir_registro_adocao,
                        4: self.alterar_registro_adocao, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_registro_adocao.tela_opcoes()]()
