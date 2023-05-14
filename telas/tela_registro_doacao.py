from datetime import date
class TelaRegistroDoacao():
    def tela_opcoes(self):
        print("-------REGISTRO DE DOAÇÃO--------")
        print("Escolha a opcao")
        print("1 - Incluir registro de doação")
        print("2 - Alterar registro de doação")
        print("3 - Listar registros de doação")
        print("4 - Excluir registro de doação")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao
    def seleciona_cachorro_ou_gato(self):
        print("Um cachorro um gato será doado?")
        print("1 - Cachorro")
        print("2 - Gato")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_registro_doacao(self):
        print("-------- DADOS REGISTRO DE DOAÇÃO ----------")
        cpf_adotante = input("Cpf do adotante: ")
        numero_chip_animal = int(input("Numero do chip do animal: "))
        motivo = int(input("Numero do chip do animal: "))
        return {"cpf": cpf_adotante, "numero_chip": numero_chip_animal, "motivo": motivo}

    def mostra_registro_doacao(self, dados_registro_doacao):
        print("CÓDIGO DO REGISTRO DE DOAÇÃO: ", dados_registro_doacao["codigo_registro"])
        print("DATA DO REGISTRO DE DOAÇÃO: ", dados_registro_doacao["data"])
        print("STATUS DO TERMO DE RESPONSABILIDADE DO REGISTRO DE DOAÇÃO: ", dados_registro_doacao["termo_responsabilidade"])
        print("CPF DO ADOTANTE DO REGISTRO DE DOAÇÃO: ", dados_registro_doacao["cpf_adotante"])

        print("\n")

    def seleciona_registro_doacao(self):
        registro = input("codigo do registro que deseja selecionar: ")
        return registro

    def mostra_mensagem(self, msg):
        print(msg)