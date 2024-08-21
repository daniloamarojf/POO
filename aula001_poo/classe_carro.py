import os


class Veiculo:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        

# Solicitando entrade de dados do usuário
os.system('cls')
print('-'*70)
marca = input('Digite a marca do veículo: ')
modelo = input('Digite o modelo do veículo: ')
ano = input('Digite o ano do modelo: ')
cor = input('Digite a cor do veículo: ')

# Criando um objeto d classe Veiculo com dados fornecidos pelo usuário
veiculo1 = Veiculo(marca, modelo, ano, cor)

# Acessando e imprimindo atributos do objeto
print('-'*70)
print('\nInfirmações do Veículo:')
print('='*70)
print(f'Marca: {veiculo1.marca}')
print(f'Modelo: {veiculo1.modelo}')
print(f'Ano: {veiculo1.ano}')
print(f'Cor: {veiculo1.cor}')
print('-'*70)