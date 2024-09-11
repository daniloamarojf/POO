# Faça um programa que imprima os valores no intervalo definidos pelo usuário.  Defina 3 números que deverão ser ignorados, ou seja, que não serão impressos na tela.

import os

class Numeros:
    def __init__(self, numero_inicial, numero_final):
        self.numero_inicial = numero_inicial
        self.numero_final = numero_final
        
    def definir_intervalo(self):
        pass
    
    def ignorar_numeros(self):
        pass
    
class Imprimir(Numeros):
    def __init__(self, numero_inicial, numero_final):
        self.numero_inicial = numero_inicial
        self.numero_final = numero_final
        
    def definir_intervalo(self):
        for var in range(self.numero_inicial, self. numero_final + 1):
            print(f'{var}', end=' | ')    
        return
    
    def ignorar_numeros(self):
        for var in range(self.numero_inicial, self.numero_final + 1):
            if var == 2:
                continue
            if var == 5:
                continue
            if var == 7:
                continue
            print(f'{var}', end=' | ')
        return
    
    os.system('cls')

numero_inicial = int(input('Número inicial: '))
numero_final = int(input('Numero final: '))

intervalo = Imprimir(numero_inicial, numero_final)
intervalo_com_ignorados = Imprimir(numero_inicial, numero_final)

print('-'*70)
print('INTERVALO DE NÚMEROS')
print(f'{intervalo.definir_intervalo()}')
print('='*70)
print('INTERVALO COM NÚMEROS IGNORADOS')
print(f'{intervalo_com_ignorados.ignorar_numeros()}')




