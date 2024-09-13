# Crie um programa que realiza a contagem de 1 até 100, usando apenas de números ímpares, 
# ao final do processo exiba na tela quantos números ímpares foram encontrados nesse intervalo, assim como a soma dos mesmos.

import os


class Numeros:
    def __init__(self, numero_inicial, numero_final):
        self.numero_inicial = numero_inicial
        self.numero_final = numero_final
        
    def impares(self):
        pass
    
    
class Imprimir(Numeros):
    def __init__(self, numero_inicial, numero_final):
        self.numero_inicial = numero_inicial
        self.numero_final = numero_final
        
    def impares(self):
        num_impar = []
        contador = 0
        soma = 0
        for var in range(self.numero_inicial, self.numero_final + 1):
            
            
            if var % 2 != 0:
                
                num_impar.append(var)
                contador = contador + 1
                soma += var
                
        print(f'{num_impar}')
        print(f'{contador}')
        print(f'{soma}')
            
            
numero_inicial = 1
numero_final = 100
    
numeros_impares = Imprimir(numero_inicial, numero_final)  

print(f'{numeros_impares.impares()}')    
    
    
