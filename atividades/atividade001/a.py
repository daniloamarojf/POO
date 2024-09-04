# Faça um programa que peça 3 valores , depois calcule e imprima  a soma e a multiplicação desses valores. 

import os

# Classe 
class Calculos:
    # Metodo construtor
    def __init__(self, numero1=0, numero2=0, numero3=0):
        self.numero1 = numero1
        self.numero2 = numero2
        self.numero3 = numero3
    
    # Método da classe para somar       
    def somar(self): 
        return self.numero1 + self.numero2 + self.numero3
    
    # Método da classe para múltiplicar
    def multiplicar(self):
        return self.numero1 * self.numero2 * self.numero3


    
os.system('cls') 
print('-'*70)
print(' SOMA E MULTIPLICAÇÃO ')
print('-'*70)
print()

# Entrada de dados
numero1 = int(input('Digite o 1º número: '))
numero2 = int(input('Digite o 2º número: '))
numero3 = int(input('Digite o 3º número: '))

# Instanciando o objeto calculos
calculos = Calculos(numero1, numero2, numero3)

# Invocando o método somar e múltiplicar
resultado_soma = calculos.somar()
resultado_produto = calculos.multiplicar()



print()   
print('-'*70)
print(' RESULTADOS ')
print('-'*70)
print()
print(f'A soma dos valores é: {resultado_soma}')
print(f'A multiplicação dos valoes é: {resultado_produto}')