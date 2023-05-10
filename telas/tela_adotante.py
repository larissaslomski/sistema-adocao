class TelaAdotante():
    def tela_opcoes(self):
        print("-------ADOTANTE--------")
        print("Escolha a opcao")
        print("1 - Incluir adotante")
        print("2 - Alterar adotante")
        print("3 - Listar adotantes")
        print("4 - Excluir adotante")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_adotante(self):
        print("-------- DADOS ADOTANTE ----------")
        cpf = input("CPF: ")
        nome = input("Nome: ")
        nascimento = input("Data de nascimento: ")
        endereco = input("Endereço: ")
        tem_outros_animais = input("Possui outros animais? S/N")
        return {"cpf": cpf, "nome": nome, "nascimento": nascimento, "endereco": endereco,
                "tem_outros_animais": tem_outros_animais}

    def mostra_adotante(self, dados_adotante):
        print("CPF DO ADOTANTE: ", dados_adotante["cpf"])
        print("NOME DO ADOTANTE: ", dados_adotante["nome"])
        print("DATA DE NASCIMENTO DO ADOTANTE: ", dados_adotante["nascimento"])
        print("ENDERECO DO ADOTANTE: ", dados_adotante["endereco"])
        # print("OUTROS ANIMAIS: ", dados_adotante["tem_outros_animais"])
        print("\n")

    def seleciona_adotante(self):
        cpf = input("CPF do adotante que deseja selecionar: ")
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)