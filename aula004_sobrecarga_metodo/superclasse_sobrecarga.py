class ClassePai:
    # Método construtor
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    # Método que vai ser sobrecarregado,
    def metodo_classe(self):
        print('Aqui vou multiplicar a e b!')
        resultado = self.a + self.b
        print(f'Este cálculo está sendo realizado')
        print(f'pelo médoto da classe Pai!')
        print(f'O resultado da soma de {self.a} e {self.b} = {resultado}')
        
        
class ClasseFilha(ClassePai):
    # Método Construtor
    def __init__(self, a, b):
        super().__init__(a,b) # Chama o contrutor da classe pai
        # Não é necessario redefinir a variável self. a e self.b,
        # pois já foram inicializada pelo construtor da calsse pai
        
    # Sobrecarga de método
    def metodo_classe(self):
        # primeiro execulta o método da classe pai
        super().metodo_classe()
        # Depois execulta o método da classe filha
        resultado = self.a + self.b
        print(f'O resultado da soma na classe Filha é: {resultado}')
        
        
# Programa principal
teste = ClasseFilha(1, 2)       
teste.metodo_classe()

        