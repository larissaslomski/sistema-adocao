class TelaSistema:
    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("-------- SISTEMA ADOÇÃO ---------")
        print("Escolha sua opcao")
        print("1 - Registrar uma adoção")
        print("2 - Registrar uma doação")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao:"))
        return opcao