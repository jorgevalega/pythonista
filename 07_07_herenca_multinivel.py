# Herença multinível
# 1° Problema
class Veiculo:
    pass
class VeiculoDeRodas(Veiculo):
    pass
class Carro(VeiculoDeRodas):
    pass
class CarroEletrico(Carro):
    pass
class CarroEletricoDuasPortas(CarroEletrico):
    pass