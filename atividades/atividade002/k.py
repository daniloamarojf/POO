# Crie um programa que pede que o usuário digite um nome ou uma frase, 
# verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em tela esse resultado.

import os


class Frase:
    def __init__(self, frase):
        self.frase = frase
        
    def verificacao(self, frase):
        pass
    
class Imprimir(Frase):
    def __init__(self, frase):
        self.frase = frase
        
    def verificacao(self):
        frase_inversa = self.frase[::-1]
        
        if self.frase == frase_inversa:
            print(f'Frase Polídromo')
        else: 
            print(f'Frase NÂO Polídromo')
            
os.system('cls')
            
frase = input('Digite o frase: ').upper()

polidromo = Imprimir(frase)

polidromo.verificacao()
        






