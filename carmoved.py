class VeiculoBase:
    def __init__(self, modelo, cor):
        self.__modelo = modelo
        self.__cor = cor
        self.__velocidade_atual = 0

    @property
    def modelo(self):
        return self.__modelo

    @property
    def cor(self):
        return self.__cor

    @property
    def velocidade_atual(self):
        return self.__velocidade_atual

    def acelerar(self, incremento):
        self.__velocidade_atual += incremento

    def desacelerar(self, decremento):
        self.__velocidade_atual -= decremento

class CarsMovedFrota:
    def __init__(self):
        self.veiculos = []

    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)

    def mostrar_informacoes(self):
        for veiculo in self.veiculos:
            print(f"{type(veiculo).__name__} - Modelo: {veiculo.modelo}, Cor: {veiculo.cor}, Velocidade Atual: {veiculo.velocidade_atual}")

# Exemplo de uso
frota = CarsMovedFrota()

carro1 = VeiculoBase("Sedan", "Prata")
carro2 = VeiculoBase("SUV", "Preto")
moto1 = VeiculoBase("Esportiva", "Vermelho")

frota.adicionar_veiculo(carro1)
frota.adicionar_veiculo(carro2)
frota.adicionar_veiculo(moto1)

carro1.acelerar(30)
carro2.acelerar(20)
moto1.acelerar(25)

frota.mostrar_informacoes()
