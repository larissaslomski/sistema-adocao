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

<<<<<<< Updated upstream
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
=======
    # Para alterar os atributos de tipo_habitacao
    # O identificador do tipo de habitacao pode ser o cpf relacionado, ou seja, o cpf também seria atributo de
    # tipo_habitacao, ja que o controlador de tipos_habitacao não conhece a classe adotante

    def incluir_tipo_habitacao(self):
        dados_adotante = self.__tela_adotante.pega_dados_adotante()
        
        cpf_valido = self.pega_adotante_por_cpf(dados_adotante['cpf'])
        if cpf_valido is None:
            tem_outros_animais = dados_adotante["tem_outros_animais"].upper()
            if tem_outros_animais == "S" or tem_outros_animais == "N":
                if tem_outros_animais == "S":
                    tem_outros_animais = True
                else:
                    tem_outros_animais = False
                adotante = Adotante(
                    dados_adotante["cpf"], dados_adotante["nome"], dados_adotante["nascimento"], dados_adotante["endereco"], tem_outros_animais)
                self.__adotantes.append(adotante)
                self.__tela_adotante.mostra_mensagem(
                    "Adotante cadastrado com sucesso no sistema")
            else:
                self.__tela_adotante.mostra_mensagem(
                    "ERRO: informações inválidas, tente novamente")
                self.__tela_adotante.pega_dados_adotante()
        else:
            self.__tela_adotante.mostra_mensagem(
                "ERRO: o Adotante ja esta cadastrado no Sistema.")

    def listar_adotantes(self):
        tam_lista_adotantes = len(self.__adotantes)
        if tam_lista_adotantes > 0:
            for adotante in self.__adotantes:
                self.__tela_adotante.mostra_adotante(
                    {"cpf": adotante.cpf, "nome": adotante.nome, "nascimento": adotante.nascimento, "endereco": adotante.endereco, "tem_outros_animais": adotante.tem_outros_animais})
        else:
            self.__tela_adotante.mostra_mensagem(
                "ERRO: Não existe nenhum adotante cadastrado no Sistema.")

    def alterar_adotante(self):
        self.listar_adotantes()
        cpf_adotante = self.__tela_adotante.seleciona_adotante()
        adotante = self.pega_adotante_por_cpf(cpf_adotante)

        if (adotante is not None):
            novos_dados_adotante = self.__tela_adotante.pega_dados_adotante()
            adotante.cpf = novos_dados_adotante["cpf"]
            adotante.nome = novos_dados_adotante["nome"]
            adotante.nascimento = novos_dados_adotante["nascimento"]
            adotante.endereco = novos_dados_adotante["endereco"]
            adotante.tem_outros_animais = novos_dados_adotante["tem_outros_animais"]
            self.listar_adotantes()
        else:
            self.__tela_adotante.mostra_mensagem(
                "ERRO: O Adotante não existe.")

    def excluir_adotante(self):
        self.listar_adotantes()
        cpf_adotante = self.__tela_adotante.seleciona_adotante()
        adotante = self.pega_adotante_por_cpf(cpf_adotante)

        if (adotante is not None):
            self.__adotantes.remove(adotante)
            self.__tela_adotante.mostra_mensagem(
                f"Adotante de cpf: {cpf_adotante} foi excluido do sistema.")
            self.listar_adotantes()
        else:
            self.__tela_adotante.mostra_mensagem(
                "ERRO: O Adotante não existe.")
>>>>>>> Stashed changes

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
<<<<<<< Updated upstream
        lista_opcoes = {1: self.cria_casa_pequena, 2: self.cria_casa_media, 3: self.cria_casa_grande, 4: self.cria_apartamento_pequeno,
                        5: self.cria_apartamento_medio, 6: self.cria_apartamento_grande, 0: self.retornar}
=======
        lista_opcoes = {0: self.retornar}
>>>>>>> Stashed changes

        continua = True
        while continua:
            lista_opcoes[self.__tela_tipo_habitacao.tela_opcoes()]()
            break
