# Faça um programa com entrada de dados para calcular o perímetro de um retângulo.
import os


class Calculos:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
        
    def perimetro(self):
        return (self.comprimento + self.largura) * 2

os.system('cls')

print('-'*70)
print('CALCULANDO PERÍMETRO')
print('-'*70)
print()


comprimento = float(input('Qual o comprimento do retângulo..: '))
largura = float(input('Qual a largura do retângulo: '))

calculo_perimetro = Calculos(comprimento, largura)
perimetro = calculo_perimetro.perimetro()

# Saida de dados
print('-'*70)
print(' RESULTADOS ')
print('-'*70)
print()
print(f'Retângulo com medidas: {comprimento} de comprimento e {largura} de largura')
print(f'seu perímetro é:   {perimetro}')