# Faça um programa que converta metros em centímetros e milímetros.
import os


# Classe
class Converter:
    # Método Construtor
    def __init__(self, medida_metros):
        self.medida_metros = medida_metros
    
    # Método converter para centímetros
    def converter_centimentros(self):
        return self.medida_metros * 100
    
    # Método converter para milímetro
    def converter_milimetros(self):
        return self.medida_metros * 1000
    

# Limpando a tela
os.system('cls')

print('*'*70)
print('CONVERTENDO METROS E CENTÍMETROS E MILÍMETROS')
print('*'*70)
print()

# Entrada de dados
medida_metros = float(input('Digite valor em metros: '))
print()

# Instanciando o objeto converter_centimetros_milimetros
converter_centimetros_milimetros = Converter(medida_metros)

# Invocando os métodos da classe Converter
centimetros = converter_centimetros_milimetros.converter_centimentros()
milimetros = converter_centimetros_milimetros.converter_milimetros()

# Saida de dados
print('-'*70)
print(' RESULTADOS ')
print('-'*70)
print()
print(f'{medida_metros} metros equivale a {centimetros} centimetros.')
print(f'{medida_metros} metros equivale a {milimetros} milímetros.')