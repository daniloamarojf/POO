# Faça um programa que some a quantidade de números pares encontrados no intervalo entre 0 e 100.

import os


# Classe 
class Numeros:
    # Método construtor
    def __init__(self, numero_inicial, numero_final):
        self.numero_inicial = numero_inicial
        self.numero_final = numero_final
    
    # Função determinar intervalo
    def intervalo(self):
        pass   
    
    # função determinar números pares            
    def numeros_pares(self):
        pass
    
     # Função somar pares
    def contar(self):
        pass
    

# Classe filha    
class Imprimir(Numeros):
    # Método construtor
    def __init__(self, numero_inicial, numero_final):
        self.numero_inicial = numero_inicial
        self.numero_final = numero_final
    
    # Função determinar intervalo
    def intervalo(self):
        intervalo = []
        for var in range(self.numero_inicial, self.numero_final+1):
            intervalo.append(var)
        return intervalo    
    
    # função determinar números pares            
    def numeros_pares(self):
        pares = []
        for var in range(self.numero_inicial, self.numero_final+1):
            if var % 2 == 0:
                pares.append(var) 
        return pares
    
    
class Contar(Numeros): 
    # Método construtor
    def __init__(self, numero_inicial, numero_final):
        self.numero_inicial = numero_inicial
        self.numero_final = numero_final  
    
    # função determinar números pares            
    def numeros_pares(self):
        pares = []
        for var in range(self.numero_inicial, self.numero_final+1):
            if var % 2 == 0:
                pares.append(var) 
        return pares
        
     # Função somar pares
    def contar(self):
        pares = self.numeros_pares()
        total_pares = len(pares)
        return total_pares

# Declarando intervalos
numero_inicial = 0
numero_final = 100 

# Instancias da classe Números e Contagem
intervalo = Imprimir(numero_inicial, numero_final)
contar_pares = Contar(numero_inicial, numero_final)

# Limpando a tela
os.system('cls')

# Saida de dados
print('-'*70)
print('RESULTADOS')
print('-'*70)
print()
print(f'Intervalos de números: {intervalo.intervalo()}\n')
print(f'Números pares:  {intervalo.numeros_pares()}\n')
print(f'Soma dos numeros pares: {contar_pares.contar()}\n')
