# Faça um algoritmo que imprima a frase "estou em looping" e, em seguida, solicite ao usuário digitar uma letra. 
# Caso a letra seja o “f" finalize a aplicação. Do contrário, imprima novamente a mesma frase até que o caractere “f" seja digitado.

import os


class Comandos:
    def __init__(self):
        self
        pass
        
    def finalizar_aplicacao(self):
        pass
    
class Imprimir(Comandos):
    def __init__(self):
        pass
        
    def finalizar_aplicacao(self):
        while True:
            sair = input('Digite "f" para finalizar: ')
            if sair == 'f':
                print('Operação finalizada')
                break
            else:
                continue
            
        return

os.system('cls')

print('Estou em looping') 
    

finalizar = Imprimir()

print('-'*70)

print(f'{finalizar.finalizar_aplicacao()}')

