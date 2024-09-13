# Sobrecarga de Métodos

class ClassePai: # super classe
    # Método construtor
    def __init__(self, a ,b):
        self.a = a
        self.b = b
        
    # Para sobrecarregar
    # vai ser usada para soma 2 números
    def metodo_classe(self, a, b):
        pass
    
    
class ClasseFilha(ClassePai): # Classe derivada
    # Método construtor
    def __int__(self, a, b):
        self.a = a
        self.b = b
        
    # Sobrecarga de Método
    def metodo_classe(self):
        return self.a + self.b
    
    
# Programa principal
teste = ClasseFilha(1, 2)
teste.metodo_classe()    
    
    
    