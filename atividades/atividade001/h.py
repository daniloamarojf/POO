# Faça um programa que receba um número inteiro, depois imprima sua tabuada de multiplicação.

import os


# Classe
class Tabuada:
    # Método construtor
    def __init__(self, numero):
        self.numero = numero
    
    # Método para multiplicar
    def multiplicar(self):
        for c in range(1, 11): 
            print(f'{c} x {self.numero} = {c * self.numero}')
        return

# Limpando a tela
os.system('cls')

print('*'*70)
print('TABUADA DE MULTIPLICAÇÃO')
print('*'*70)
print()

# Entrada de dados
numero = int(input('Digite um numero: '))

# Instanciando o objeto tabuada_multiplicaçao 
tabuada_multiplicao = Tabuada(numero)

# Saida de dados
print('-'*70)
print(' RESULTADOS')
print('-'*70)
print()
print(f'TABUADA DE MULTIPLICAÇÃO DO {numero}')
multiplicacao = tabuada_multiplicao.multiplicar()
