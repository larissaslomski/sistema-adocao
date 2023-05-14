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
    def seleciona_cachorro_ou_gato(self):
        print("Um cachorro um gato será adotado?")
        print("1 - Cachorro")
        print("2 - Gato")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_registro_adocao(self):
        print("-------- DADOS REGISTRO DE ADOÇÃO ----------")
        cpf_adotante = input("Cpf do adotante: ")
        numero_chip_animal = int(input("Numero do chip do animal: "))
        return {"cpf": cpf_adotante, "numero_chip": numero_chip_animal}

    def mostra_registro_adocao(self, dados_registro_adocao):
        print("CÓDIGO DO REGISTRO DE ADOÇÃO: ", dados_registro_adocao["codigo_registro"])
        print("DATA DO REGISTRO DE ADOÇÃO: ", dados_registro_adocao["data"])
        print("STATUS DO TERMO DE RESPONSABILIDADE DO REGISTRO DE ADOÇÃO: ", dados_registro_adocao["termo_responsabilidade"])
        print("CPF DO ADOTANTE DO REGISTRO DE ADOÇÃO: ", dados_registro_adocao["cpf_adotante"])

        print("\n")

    def seleciona_registro_adocao(self):
        registro = input("codigo do registro que deseja selecionar: ")
        return registro

    def mostra_mensagem(self, msg):
        print(msg)