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

    def pega_dados_adotante(self):
        print("-------- DADOS REGISTRO DE ADOÇÃO ----------")
        codigo_registro = input("Código do registro de adoção: ")
        data = date.today()
        nascimento = input("Data de nascimento: ")
        endereco = input("Endereço: ")
        tem_outros_animais = input("Possui outros animais? S/N")
        return {"codigo_registro": codigo_registro, "nome": nome, "nascimento": nascimento, "endereco": endereco}

    def mostra_adotante(self, dados_adotante):
        print("CÓDIGO DO REGISTRO DE ADOÇÃO: ", dados_adotante["codigo_registro"])
        print("NOME DO REGISTRO DE ADOÇÃO: ", dados_adotante["nome"])
        print("FONE DO REGISTRO DE ADOÇÃO: ", dados_adotante["nascimento"])
        print("CPF DO REGISTRO DE ADOÇÃO: ", dados_adotante["endereco"])
        print("\n")

    def seleciona_adotante(self):
        cpf = input("CPF do adotante que deseja selecionar: ")
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)