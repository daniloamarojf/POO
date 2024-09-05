# Faça um programa que receba um valor em reais, depois calcule quantos dólares daria para comprar com esse valor.
import os


class Convercao:
    def __init__(self, valor_real, dolar):
        self.valor_real = valor_real
        self.dolar = dolar
        
    def para_dolar(self):
        return self.valor_real / self.dolar
        
# limpando a tela
os.system('cls')

print('-'*70)
print('CONVERTENDEO REAIS EM DÓLAR')
print('-'*70)
print()

# Entrada de dados
valor_real = float(input('Digite um valor em reais: R$ '))
dolar = float(input('Digite o valor atual do dolar: US$ '))

# Criando uma instância da classe Conversão
converter_dolar = Convercao(valor_real, dolar)
converter = converter_dolar.para_dolar()

# Saidas
print('-'*70)
print(' RESULTADO ')
print('-'*70)
print()
print(f'Com R$ {valor_real:.2f} compramos {converter:.2f} dólares.')