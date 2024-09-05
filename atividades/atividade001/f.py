# Faça um programa que receba um número qualquer e calcule o dobro e o triplo desse número.
import os


class Calculos:
    def __init__(self, numero):
        self.numero = numero
        
    def calcular_dobro(self):
        return self.numero * 2
    
    def calcular_triplo(self):
        return self.numero * 3
    


# Limpando a tela
os.system('cls')

print('*'*70)
print('CALCULO DOBRO E TRIPLO')
print('*'*70)
print()

# Entrada de dados
numero = float(input('Digite um numero: '))
print()

calcular_dobro_triplo = Calculos(numero)
dobro = calcular_dobro_triplo.calcular_dobro()
triplo = calcular_dobro_triplo.calcular_triplo()

# Saída
print('-'*70)
print(' RESULTADO ')
print('-'*70)
print(f' O dobro do numero {numero} é: {dobro}')
print(f' O triplo de numero {numero} é: {triplo}')