# Faça um programa que calcule os números primos em um intervalo pré-determinado pelo usuário.

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
        primos = []
        for var in range(self.numero_inicial, self.numero_final + 1):
            contar = 0
            for var1 in range(self.numero_inicial + 1, self.numero_final + 1):
                if var % var1 == 0:
                    contar = contar + 1
            
            if contar == 2:  
                primos.append(var)  
        return primos
    
os.system('cls')    
    
numero_inicial = int(input('Número inicial: '))     
numero_final = int(input('Número final: '))

numeros_primos = Imprimir(numero_inicial, numero_final)



print('-'*70)
print(f'Números primos entre {numero_inicial} e {numero_final}')
print('-'*70)
print()
print(f'{numeros_primos.determinar_primos()}')
                    