# Faça um programa que receba um número inteiro e mostre o sucessor e antecessor.
import os


class Calculos:
    def __init__(self, numero):
        self.numero = numero
        
    def mostrar_sucessor(self):
        return self.numero + 1
    
    def mostrar_antecessor(self):
        return self.numero - 1
    
# Limpando a tela
os.system('cls')

print('*'*70)
print('SUCESSOR E ANTECESSOR')
print('*'*70)

# Entrada de dados
numero = int(input('Digite um numero: '))

calculando_sucessor_antecessor = Calculos(numero)
sucessor = calculando_sucessor_antecessor.mostrar_sucessor()
antecessor = calculando_sucessor_antecessor.mostrar_antecessor()

# Saída
print('-'*70)
print(' RESULTADO ')
print('-'*70)
print(f'O antecessor de {numero} é {antecessor} e o sucessor {sucessor}')