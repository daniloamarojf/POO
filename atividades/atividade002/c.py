# Faça um programa que imprima os números no intervalo entre 1 e 10 em ordem inversa.

import os


# Classe
class Numeros:
    # Método construtor
    def __init__(self, numero_inicial, numero_final, ordem):
        self.numero_inicial = numero_inicial
        self.numero_final = numero_final
        self.ordem = ordem
    
    # Método da classe par inverter ordem    
    def determinar_inverso(self):
        pass
    
    
class Imprimir(Numeros):
    def __init__(self, numero_inicial, numero_final, ordem):
        self.numero_inicial = numero_inicial
        self.numero_final = numero_final
        self.ordem = ordem
        
    def determinar_inverso(self):
        if self.ordem == -1: # Condição para extrutura de repetição varrer de forma inversa
            for var in range(self.numero_final, self.numero_inicial-1, -1):
                print(f'{var}', end=' | ')
        return
        
    

# Instanciando o objeto ordem inversa    
ordem_inversa = Imprimir(1, 10, -1)

# Limpando a tela
os.system('cls')

# Saida de dados
print('-'*70)
print(f'NÚMEROS DE {ordem_inversa.numero_inicial} A {ordem_inversa.numero_final} INVERSO.')
print('-'*70)
ordem_inversa.determinar_inverso() # Chamando o método determinar inverso