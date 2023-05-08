class TelaCachorro():
    def tela_opcoes(self):
        print("-------CACHORRO --------")
        print("Escolha a opcao")
        print("1 - Incluir cachorro")
        print("2 - Alterar cachorro")
        print("3 - Listar cachorros")
        print("4 - Excluir cachorro")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_cachorro(self):
        print("-------- DADOS CACHORRO ----------")
        nome = input("Nome: ")
        raca = input("Raça: ")
        tamanho = input("Endereço: ")
        return {"nome": nome, "raca": raca, "tamanho": tamanho}

    def mostra_cachorro(self, dados_cachorro):
        print("NUMERO CHIP DO CACHORRO: ", dados_cachorro["numero chip"])
        print("NOME DO CACHORRO: ", dados_cachorro["nome"])
        print("RAÇA DO CACHORRO: ", dados_cachorro["raca"])
        print("TAMANHO DO CACHORRO: ", dados_cachorro["tamanho"])
        print("\n")

    def seleciona_cachorro(self):
        numero_chip = input("Numero do chip do cachorro que deseja selecionar: ")
        return numero_chip

    def mostra_mensagem(self, msg):
        print(msg)
