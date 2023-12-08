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
        """Converte os atributos do veículo em um dicionário."""
        return {
            "modelo": self.__modelo,
            "cor": self.__cor,
            "velocidade_atual": self.__velocidade_atual
        }

    @classmethod
    def from_dict(cls, veiculo_dict):
        """Cria uma instância de VeiculoBase a partir de um dicionário."""
        return cls(veiculo_dict["modelo"], veiculo_dict["cor"])

class CarsMovedFrota:
    def __init__(self, nome_arquivo="frota.json"):
        self.veiculos = []
        self.nome_arquivo = nome_arquivo

    def adicionar_veiculo(self, veiculo):
        """Adiciona um veículo à frota e salva as alterações."""
        self.veiculos.append(veiculo)
        self._salvar_frota()

    def mostrar_informacoes(self):
        """Exibe informações detalhadas sobre cada veículo na frota."""
        for veiculo in self.veiculos:
            print(f"{type(veiculo).__name__} - Modelo: {veiculo.modelo}, Cor: {veiculo.cor}, Velocidade Atual: {veiculo.velocidade_atual}")

    def gerar_relatorio(self):
        """Gera um relatório em formato de lista de dicionários."""
        relatorio = []
        for veiculo in self.veiculos:
            relatorio.append(veiculo.to_dict())
        return relatorio

    def _salvar_frota(self):
        """Salva os dados da frota em um arquivo JSON."""
        with open(self.nome_arquivo, "w") as arquivo:
            json.dump(self.gerar_relatorio(), arquivo)

    def carregar_frota(self):
        """Carrega a frota a partir de um arquivo JSON, se existir."""
        try:
            with open(self.nome_arquivo, "r") as arquivo:
                dados = json.load(arquivo)
                for veiculo_dict in dados:
                    veiculo = VeiculoBase.from_dict(veiculo_dict)
                    self.veiculos.append(veiculo)
        except FileNotFoundError:
            print("Arquivo de frota não encontrado. Inicializando uma nova frota.")

# Exemplo de uso
frota = CarsMovedFrota()

# Carregar frota existente ou criar uma nova
frota.carregar_frota()

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
