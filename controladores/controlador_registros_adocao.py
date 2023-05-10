from entidades.registro_adocao import RegistroAdocao
from telas.tela_registro_adocao import TelaRegistroAdocao


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

    def incluir_registro_adocao(self):
        self.__controlador_sistema.controlador_amigos.lista_amigos()
        self.__controlador_sistema.controlador_livros.lista_livro()
        dados_emprestimo = self.__tela_emprestimo.pega_dados_emprestimo()

        amigo = self.__controlador_sistema.controlador_amigos.pega_amigo_por_cpf(dados_emprestimo["cpf"])
        livro = self.__controlador_sistema.controlador_livros.pega_livro_por_codigo(dados_emprestimo["codigo"])
        if (amigo is not None and livro is not None):
            emprestimo = Emprestimo(amigo, livro, randint(0, 100))
            self.__emprestimos.append(emprestimo)
        else:
            self.__tela_emprestimo.mostra_mensagem("Dados invalidos")