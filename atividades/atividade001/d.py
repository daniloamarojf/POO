# Faça um programa que receba e divida 2 números. A saída da divisão precisará ser formatada com 4 casas decimais.
import os


# Classes
class Calculos:
    # Método Construtor
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
    
    # método da classe para dividir     
    def dividir(self):
        return self.numero1 / self.numero2

## Limpando a tela    
os.system('cls')
print('-'*70)
print('DIVISÃO DE NÚMEROS')
print('-'*70)
print()

# Entrada d dados
numero1 = float(input('Digite o 1º Número: '))
numero2 = float(input('Digite o 2º Número: '))

# Instancando o objeto da classe
calcular_divisao = Calculos(numero1, numero2)

# Invocando o método divisão 
divisao = calcular_divisao.dividir()


# Saida
print('-'*70)
print(' RESULTADO ')
print('-'*70)
print()
print(f'O resultado da divisão é: {divisao:.4f}')