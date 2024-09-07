# Faça um programa que imprima os números no intervalo entre 1 e 100. Os números devem ser apresentados na horizontal.

import os


# Classe
class Numeros:
    # Método constutor
    def __init__(self, numero_inicial, numero_final):
        self.numero_inicial = numero_inicial
        self.numero_final = numero_final
    
    # Método da classe para determinar intervalo numérico    
    def determinar_intervalo(self):
        for var in range(self.numero_inicial, self.numero_final+1):
            print(f'{var}', end=" | ")
        return

# Instanciando o objeto interalo
intervalo = Numeros(1, 100)

# Saída de dados
print('-'*70)
print(f'NÚMEROS ENTRE  {intervalo.numero_inicial} e {intervalo.numero_final}')
print('-'*70)
intervalo.determinar_intervalo() # invocando o método determinar intervalo
print()

