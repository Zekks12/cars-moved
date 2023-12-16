import json

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
            def to_dict(self):
                return {
                    "modelo": self.__modelo,
                    "cor": self.__cor,
                    "velocidade_atual": self.__velocidade_atual
                }
    @classmethod
    def from_dict(cls, veiculo_dict):
        return cls(veiculo_dict["modelo"], veiculo_dict["cor"])
class Carro(VeiculoBase):
            def acelerar(self, incremento):
                super().acelerar(2 * incremento)
            def desacelerar(self, decremento):
                super().desacelerar(decremento)
class Moto(VeiculoBase):
            def acelerar(self, incremento):
                super().acelerar(incremento)
            def desacelerar(self, decremento):
                super().desacelerar(2 * decremento)
class CarsMovedFrota:
            def __init__(self, nome_arquivo="frota.json"):
                self.veiculos = []
                self.nome_arquivo = nome_arquivo
            def adicionar_veiculo(self, veiculo):
                self.veiculos.append(veiculo)
                self._salvar_frota()
            def mostrar_informacoes(self):
        for veiculo in self.veiculos:
            print(f"{type(veiculo).__name__} - Modelo: {veiculo.modelo}, Cor: {veiculo.cor}, Velocidade Atual: {veiculo.velocidade_atual}")
    def gerar_relatorio(self):
        relatorio = []
        for veiculo in self.veiculos:
            relatorio.append(veiculo.to_dict())
        return relatorio
    def _salvar_frota(self):
        with open(self.nome_arquivo, "w") as arquivo:
            json.dump(self.gerar_relatorio(), arquivo)
    def carregar_frota(self):
        try:
            with open(self.nome_arquivo, "r") as arquivo:
                dados = json.load(arquivo)
                for veiculo_dict in dados:
                    veiculo = VeiculoBase.from_dict(veiculo_dict)
                    self.veiculos.append(veiculo)
        except FileNotFoundError:
            print("Arquivo de frota não encontrado. Inicializando uma nova frota.")

frota = CarsMovedFrota()
frota.carregar_frota()
carro1 = Carro("Sedan", "Prata")
carro2 = Carro("SUV", "Preto")
moto1 = Moto("Esportiva", "Vermelho")
frota.adicionar_veiculo(carro1)
frota.adicionar_veiculo(carro2)
frota.adicionar_veiculo(moto1)
carro1.acelerar(30)
carro2.acelerar(20)
moto1.acelerar(25)
frota.mostrar_informacoes()
