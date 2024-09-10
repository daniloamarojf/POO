# Faça um programa que imprima os números primos entre 0 e 100.

import os


class Numeros:
    def __init__(self, numero_inicial, numero_final):
        self.numero_inicial = numero_inicial
        self.numero_final = numero_final
        
    def determinar_primos(self):
        pass
    
    
class Imprimir(Numeros):
    def __init__(self, numero_inicial, numero_final):
        self.numero_inicial = numero_inicial
        self.numero_final = numero_final
        
    def determinar_primos(self):
        contar = 0
        primos = []
        for var in range(self.numero_inicial, self.numero_final):
            for var in range(self.numero_inicial, self.numero_final):
                contar = contar + 1
                
        if contar == 2:
            primos.append(var)
        return primos


numero_inicial = 0
numero_final = 100

numeros_primos = Imprimir(numero_inicial, numero_final)


os.system('cls')

print('-'*70)
print('NÚMEROS PRIMOS ENTRE 0 E 100')
print()
print(f'{numeros_primos.determinar_primos()}')


