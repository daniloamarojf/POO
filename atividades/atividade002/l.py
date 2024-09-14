# Faça um programa que verifique se o usuário e senha estão inseridos em um banco de dados (fake).
# O usuário só terá acesso se digitar os dados corretos e, assim, sair do laço.

import os

# Classe Pai
class Usuario:
    def __init__(self, usuario_correto, senha_correta):
        self.usuario_correto = usuario_correto
        self.senha_correta = senha_correta
        
    def verificacao(self, usuario_correto, senha_correta):
        pass
    
class Acesso(Usuario):
    def __init__(self, usuario_correto, senha_correta):
        self.usuario_correto = usuario_correto
        self.senha_correta = senha_correta
        
    def verificacao(self):
        
        while True:
            usuario = input('Usuário: ')
            senha = str(input('Senha: '))       
            if usuario == self.usuario_correto and senha == self.senha_correta:
                print('Usuário e senha estão corretos!')
                break
            else:
                print('Dados incorretos. Continue ...')
                print()
                
            
os.system('cls')

usuario_correto = 'Danilo'
senha_correta = '1234'


verificar = Acesso(usuario_correto, senha_correta)

verificar.verificacao()
                