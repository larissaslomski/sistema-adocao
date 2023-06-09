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

    def verifica_tipo_habitacao(self, adotante, animal):
        if animal.tamanho == "G" and str(adotante.tipo_habitacao) == "apartamento pequeno":
            verifica = False
        else:
            verifica = True

        if verifica:
            return True
        else:
            self.__tela_registro_adocao.mostra_mensagem(
                f"ATENÇAO: O tipo de habitação é inadequado.")
            self.retornar()

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
                verifica = True
            else:
                verifica = False
        except ValueError:
            self.__tela_registro_adocao.mostra_mensagem(
                "Formato de data inválido. Utilize o formato dd/mm/aaaa.")
        if verifica:
            return True
        else:
            self.__tela_registro_adocao.mostra_mensagem(
                f"ATENÇAO: Somente maiores de idade podem adotar.")
            self.retornar()

    def verifica_se_nao_doou(self, adotante):
        if self.__controlador_sistema.controlador_registros_doacao.pega_registro_doacao_por_doador(adotante) is None:
            verifica = True
        else:
            verifica = False

        if verifica:
            return True
        else:
            self.__tela_registro_adocao.mostra_mensagem(
                f"ATENÇAO: O adotante já fez uma doaçao e não pode adotar.")
            self.retornar()

    def verifica_vacinas(self, animal):
        quantidade_vacina = len(animal.historicos_vacinacao)
        if quantidade_vacina == 3:
            verifica = True
        else:
            verifica = False

        if verifica:
            return True
        else:
            self.__tela_registro_adocao.mostra_mensagem(
                f"ATENÇAO: O animal não tem as três vacinas necessárias.")
            self.retornar()

    def incluir_registro_adocao(self):
        cachorro_ou_gato = self.__tela_registro_adocao.seleciona_cachorro_ou_gato()
        while True:
            if cachorro_ou_gato not in (1, 2):
                self.__tela_registro_adocao.mostra_mensagem(
                    "Opção inválida! Selecione 1 ou 2!")
                cachorro_ou_gato = self.__tela_registro_adocao.seleciona_cachorro_ou_gato()
            else:
                break
        self.__controlador_sistema.controlador_adotantes.listar_adotantes()
        if cachorro_ou_gato == 1:
            self.__controlador_sistema.controlador_cachorros.listar_cachorros()
            dados_registro_adocao = self.__tela_registro_adocao.pega_dados_registro_adocao()
            adotante = self.__controlador_sistema.controlador_adotantes.pega_adotante_por_cpf(
                dados_registro_adocao["cpf"])
            cachorro = self.__controlador_sistema.controlador_cachorros.pega_cachorro_por_num_chip(
                dados_registro_adocao["numero_chip"])
            if adotante is not None and cachorro is not None:
                # Faz as verificaçoes necessarias para adoçao
                self.verifica_tipo_habitacao(adotante, cachorro)
                self.verifica_maior_idade(adotante.nascimento)
                self.verifica_vacinas(cachorro)
                self.verifica_se_nao_doou(adotante)
                # Cria o Registro de Adocao
                codigo_registro = uuid4().int
                data = date.today()
                registro_adocao = RegistroAdocao(
                    codigo_registro, data, cachorro, adotante, False)
                self.__registros_adocao.append(registro_adocao)
                # Coleta a assinatura do termo de responsabilidade
                self.assinar_termo_responsabilidade(codigo_registro)
                self.__controlador_sistema.controlador_cachorros.cachorros.remove(
                    cachorro)  # Remove o animal da lista de animais disponíveis
                self.__tela_registro_adocao.mostra_mensagem(
                    f"Inclusão de registro de adoção realizada com sucesso.")
            else:
                self.__tela_registro_adocao.mostra_mensagem(
                    "ERRO: Os dados que você forneceu estão incorretos.")
        elif cachorro_ou_gato == 2:
            self.__controlador_sistema.controlador_gatos.listar_gatos()
            dados_registro_adocao = self.__tela_registro_adocao.pega_dados_registro_adocao()
            adotante = self.__controlador_sistema.controlador_adotantes.pega_adotante_por_cpf(
                dados_registro_adocao["cpf"])
            gato = self.__controlador_sistema.controlador_gatos.pega_gato_por_num_chip(
                dados_registro_adocao["numero_chip"])
            if adotante is not None and gato is not None:
                # Faz as verificaçoes necessarias para adoçao
                self.verifica_maior_idade(adotante.nascimento)
                self.verifica_vacinas(gato)
                self.verifica_se_nao_doou(adotante)
                # Cria o Registro de Adocao
                codigo_registro = uuid4().int
                data = date.today()
                registro_adocao = RegistroAdocao(
                    codigo_registro, data, gato, adotante, False)
                self.__registros_adocao.append(registro_adocao)
                # Coleta a assinatura do termo de responsabilidade
                self.assinar_termo_responsabilidade(codigo_registro)
                self.__controlador_sistema.controlador_gatos.gatos.remove(
                    gato)  # Remove o animal da lista de animais disponíveis
                self.__tela_registro_adocao.mostra_mensagem(
                    f"Inclusão de registro de adoção realizada com sucesso.")
            else:
                self.__tela_registro_adocao.mostra_mensagem(
                    "ERRO: Os dados que você forneceu estão incorretos.")

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

    def assinar_termo_responsabilidade(self, cod_registro_adocao):
        registro_adocao = self.pega_registro_adocao_por_codigo(
            cod_registro_adocao)
        if registro_adocao is not None:
            while True:
                assinatura = self.__tela_registro_adocao.pega_assinatura_termo_responsabilidade()
                if assinatura.upper() == "S":
                    assinatura = True
                    registro_adocao.termo_responsabilidade = assinatura
                    self.__tela_registro_adocao.mostra_mensagem(
                        "Termo de responsabilidade assinado com sucesso!")
                    break
                else:
                    self.__tela_registro_adocao.mostra_mensagem(
                        "ATENÇAO: Você deve assinar o termo para seguir com a adoção. Registro cancelado.")
                    self.__registros_adocao.remove(registro_adocao)
                    self.retornar()
        else:
            self.__tela_registro_adocao.mostra_mensagem(
                "O registro de adoção nao esta cadastrado no Sistema.")

    def gerar_relatorio_adocao(self):
        # Dados quantidade de animais adotados por periodo
        data_inicial = self.__tela_registro_adocao.pega_datas_relatorio(
            "Data Inicial")
        data_final = self.__tela_registro_adocao.pega_datas_relatorio(
            "Data Final")
        cont = 0
        for registro in self.__registros_adocao:
            if registro.data > data_inicial and registro.data < data_final:
                cont += 1
        self.__tela_registro_adocao.mostra_mensagem(
            f"Entre {data_inicial} e {data_final} foram adotados {cont} animais.")
        # Dados animais disponiveis para adoçao
        self.__tela_registro_adocao.mostra_mensagem(
            "-------- ANIMAIS DISPONÍVEIS PARA ADOÇAO --------")
        self.__tela_registro_adocao.mostra_mensagem(
            "-------- CACHORROS --------")
        tam_lista_cachorros = len(
            self.__controlador_sistema.controlador_cachorros.cachorros)
        if tam_lista_cachorros > 0:
            self.__controlador_sistema.controlador_cachorros.listar_cachorros()
        else:
            self.__tela_registro_adocao.mostra_mensagem(
                "ATENÇAO: Não existe nenhum cachorro disponivel para adoçao.")
        self.__tela_registro_adocao.mostra_mensagem(
            "-------- GATOS --------")
        tam_lista_gatos = len(
            self.__controlador_sistema.controlador_gatos.gatos)
        if tam_lista_gatos > 0:
            self.__controlador_sistema.controlador_gatos.listar_gatos()
        else:
            self.__tela_registro_adocao.mostra_mensagem(
                "ATENÇAO: Não existe nenhum gato disponivel para adoçao.")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_registro_adocao, 2: self.listar_registro_adocao, 3: self.excluir_registro_adocao,
                        4: self.gerar_relatorio_adocao, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_registro_adocao.tela_opcoes()
            while opcao_escolhida not in (1, 2, 3, 4, 0):
                self.__tela_registro_adocao.mostra_mensagem(
                    "ERRO: Opção inválida, tente novamente.")
                opcao_escolhida = self.__tela_registro_adocao.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
