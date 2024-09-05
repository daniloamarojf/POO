# Faça um programa que peça 4 notas, após a entrada de dados calcular a média das notas digitadas.

import os


# Classe
class Calculos:
    # Método construtor
    def __init__(self, nota1, nota2, nota3, nota4):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        
    # Método da classe para calcular média
    def calcular_média(self):
        return (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4

# Limpando a tela    
os.system('cls')
print('-'*70)
print('CALCULANDO A MÉDIA DAS NOTAS')
print('='*70)
print()

# Entrada de dados
nota1 = float(input('Digite a 1º nota: '))
nota2 = float(input('Digite a 2º nota: '))
nota3 = float(input('Digite a 3º nota: '))        
nota4 = float(input('Digite a 4º nota: '))

# Instanciando o objeto calculo_média 
calculo_media = Calculos(nota1, nota2, nota3, nota4 )

# Invocando o método média
media = calculo_media.calcular_média()

# Saída
print('-'*70)
print(' RESULTADO ')
print('-'*70)
print()
print(f'A média das notas é {media}')