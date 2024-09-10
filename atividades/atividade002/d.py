# Faça um programa que imprima os números pares entre 0 e 100.

import os


class Numeros:
    # Método construtor
    def __init__(self, numero_inicial, numero_final):
        self.numero_inicial = numero_inicial
        self.numero_final = numero_final
    
    # Método da classe para determinar os pares    
    def determinar_pares(self):
        pass
    
    
class Imprimir(Numeros):
    # Método construtor
    def __init__(self, numero_inicial, numero_final):
        self.numero_inicial = numero_inicial
        self.numero_final = numero_final
    
    # Método da classe para determinar os pares    
    def determinar_pares(self):
        for var in range(self.numero_inicial, self.numero_final+1):
            if var % 2 == 0:
                print(f'{var}', end=' | ')
        return
    

# Instanciando o objeto pares    
pares = Imprimir(0, 100)

# Limpando a terminal
os.system('cls')        

# Saida de dados
print('-'*70)
print(f'NÚMEROS PARES ENTRE {pares.numero_inicial} e {pares.numero_final}')
print('-'*70)
pares.determinar_pares() #  Chamando o método determinar pares