# Faça um programa que peça o ano do seu nascimento e calcule a sua idade.

import os
import datetime


# Classe 
class Calculos:
    # Método construtor
    def __init__(self, ano_atual, ano_nascimento):
        self.ano_atual = ano_atual
        self.ano_nascimento = ano_nascimento
    
    # Método da classe para calcular idade 
    def calcular_idade(self):
        return self.ano_atual - self.ano_nascimento
    
# Limpando a tela
os.system('cls')

print('*'*70)
print('CÁLCULO DE IDADE')
print('*'*70)

# Entrada de dados
ano_atual = datetime.datetime.now().year
ano_nascimento = int(input('Digite o ano de nascimento: '))


calculo_idade = Calculos(ano_atual, ano_nascimento)

idade = calculo_idade.calcular_idade()

# Saída
print('-'*70)
print(' RESULTADO ')
print('-'*70)
print()
print(f'Você possui {idade} anos.')