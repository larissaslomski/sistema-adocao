from datetime import date
class TelaRegistroAdocao():
    def tela_opcoes(self):
        print("-------REGISTRO DE ADOÇÃO--------")
        print("Escolha a opcao")
        print("1 - Incluir registro de adoção")
        print("2 - Alterar registro de adoção")
        print("3 - Listar registros de adoção")
        print("4 - Excluir registro de adoção")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_registro_adocao(self):
        print("-------- DADOS REGISTRO DE ADOÇÃO ----------")
        #vamos criar codigo de maneira aleatoria?
        codigo_registro = input("Código do registro de adoção: ")
        data = date.today()
        return {"codigo_registro": codigo_registro, "data": data}

    def mostra_registro_adocao(self, dados_registro_adocao):
        print("CÓDIGO DO REGISTRO DE ADOÇÃO: ", dados_registro_adocao["codigo_registro"])
        print("NOME DO REGISTRO DE ADOÇÃO: ", dados_registro_adocao["data"])
        print("\n")

    def seleciona_registro_adocao(self):
        registro = input("codigo do adotante que deseja selecionar: ")
        return registro

    def mostra_mensagem(self, msg):
        print(msg)