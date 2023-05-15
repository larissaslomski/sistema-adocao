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

    def pega_data_nascimento_adotante(self):
        print("-------- DADOS NASCIMENTO DO ADOTANTE --------")
        ano_nascimento = input("Ano de nascimento com quatro dígitos: ")
        mes_nascimento = input("Mês de nascimento com dois dígitos: ")
        dia_nascimento = input("Dia de nascimento com dois dígitos: ")
        return ano_nascimento, dia_nascimento, mes_nascimento

    def pega_dados_adotante(self):
        print("-------- DADOS ADOTANTE --------")
        cpf = input("CPF: ")
        nome = input("Nome: ")
        endereco = input("Endereço: ")
        tem_outros_animais = input("Possui outros animais?(S/N) ")
        return {"cpf": cpf, "nome": nome, "endereco": endereco,
                "tem_outros_animais": tem_outros_animais}

    def pega_dados_adotante_alt(self):
        print("-------- DADOS ADOTANTE --------")
        nome = input("Nome: ")
        nascimento = input("Data de nascimento: ")
        endereco = input("Endereço: ")
        tem_outros_animais = input("Possui outros animais?(S/N) ")
        return {"nome": nome, "nascimento": nascimento, "endereco": endereco,
                "tem_outros_animais": tem_outros_animais}

    def mostra_adotante(self, dados_adotante):
        print("------------------------------------")
        print("\n")
        print("CPF DO ADOTANTE: ", dados_adotante["cpf"])
        print("NOME DO ADOTANTE: ", dados_adotante["nome"])
        print("DATA DE NASCIMENTO DO ADOTANTE: ", dados_adotante["nascimento"])
        print("ENDERECO DO ADOTANTE: ", dados_adotante["endereco"])
        print("OUTROS ANIMAIS: ", dados_adotante["tem_outros_animais"])
        print("TIPO DE HABITACAO: ", dados_adotante["tipo_habitacao"])
        print("\n")

    def seleciona_adotante(self):
        cpf = input("CPF do adotante que deseja selecionar: ")
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)
