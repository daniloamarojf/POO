# Evolua o programa anterior para um código que pergunte ao usuário qual o intervalo que ele deseja ver  impresso.

import os


# Classe
class Numeros:
    # Método construtor
    def __init__(self, numero_inicial, numero_final):
        self.numero_inicial = numero_inicial
        self.numero_final = numero_final
    
    # Método da classe para determinar intervalo numérico
    def determinar_intervalo(self):
        for var in range(self.numero_inicial, self.numero_final+1):
            print(f'{var}', end=' | ')
        return 
        
print('-'*70)
print('IMPRESSÃO DE INTERVALO NUMÉRICO')
print('-'*70)
numero_inicial = int(input('Número inicial: ')) # Entrada de dados
numero_final = int(input('Número final: ')) # Entrada de dados

# Instanciando o objeto intervalo
intervalo = Numeros(numero_inicial, numero_final)

# Saída de dados
print('='*70)
print(f'NÚMEROS ENTRE {intervalo.numero_inicial} A {intervalo.numero_final}')
print('='*70)
intervalo.determinar_intervalo() # Invocando método determinar intervalo