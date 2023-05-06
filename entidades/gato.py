from entidades.animal import Animal
from entidades.historico_vacinacao import HistoricoVacinacao


class Gato(Animal):
    def __init__(self, numero_chip: int, nome: str, raca: str, historico_vacinacao: HistoricoVacinacao):
        super().__init__(numero_chip, nome, raca, historico_vacinacao)
