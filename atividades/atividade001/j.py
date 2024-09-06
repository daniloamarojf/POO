# Faça um programa com entrada de dados para calcular o perímetro de um retângulo.
import os


# Classe
class Calculos:
    # Método construtor
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
    
    # Método para calcular o perímetro
    def perimetro(self):
        return (self.comprimento + self.largura) * 2

# Limpando a tela
os.system('cls')

print('-'*70)
print('CALCULANDO PERÍMETRO')
print('-'*70)
print()

# Entrada de dados
comprimento = float(input('Qual o comprimento do retângulo..: '))
largura = float(input('Qual a largura do retângulo: '))

# Instanciando o objeto calcular_perímetro
calculo_perimetro = Calculos(comprimento, largura)

# chamando o método perimetro
perimetro = calculo_perimetro.perimetro()

# Saida de dados
print('-'*70)
print(' RESULTADOS ')
print('-'*70)
print()
print(f'Retângulo com medidas: {comprimento} de comprimento e {largura} de largura')
print(f'seu perímetro é:   {perimetro}')