# Faça um programa que receba um número inteiro e mostre o sucessor e antecessor.
import os

# Classe
class Calculos:
    # Método construtor
    def __init__(self, numero):
        self.numero = numero
    
    # Método da classe para mostar o número sucessor    
    def mostrar_sucessor(self):
        return self.numero + 1
    
    # Método da classe apra mostar o número antecessor
    def mostrar_antecessor(self):
        return self.numero - 1
    
# Limpando a tela
os.system('cls')

print('*'*70)
print('SUCESSOR E ANTECESSOR')
print('*'*70)

# Entrada de dados
numero = int(input('Digite um numero: '))

# Instanciando um objeto da classe Calculos
calculando_sucessor_antecessor = Calculos(numero)

# Invocando os métodos da classe
sucessor = calculando_sucessor_antecessor.mostrar_sucessor()
antecessor = calculando_sucessor_antecessor.mostrar_antecessor()

# Saída
print('-'*70)
print(' RESULTADO ')
print('-'*70)
print(f'O antecessor de {numero} é {antecessor} e o sucessor {sucessor}')