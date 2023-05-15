from datetime import datetime


def verificar_idade(data_nascimento):
    data_atual = datetime.now().date()
    idade_minima = 18
    try:
        data_formatada = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
        diferenca_anos = data_atual.year - data_formatada.year
        if (data_atual.month, data_atual.day) < (data_formatada.month, data_formatada.day):
            diferenca_anos -= 1
        if diferenca_anos >= idade_minima:
            print("Você tem mais de 18 anos!")
        else:
            print("Você tem menos de 18 anos.")
    except ValueError:
        print("Formato de data inválido. Utilize o formato dd/mm/aaaa.")


# Exemplo de uso
data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
verificar_idade(data_nascimento)