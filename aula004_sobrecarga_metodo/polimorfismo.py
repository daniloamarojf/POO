from math import pi

# Define a classe base Forma com método área
# que não faz nada (é quase uma classe abstrata)


class Forma:
    def area(self):
        pass
    

# Define a classe Círculo que herda de Forma
# O construtor __init__ inicializa o atributo raio
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
        
    # Define o método área para calcular a área do      
    # círculo usando a formula PI * raio2
    def area(self):
        return pi * (self.raio ** 2)
    
    
    
# Define a classe retangulo que herda de FOrma
class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        
    # Define o métodod para calcular a area
    # do retangulo usando a fórmula largura * altura
    def area(self):
        return self.largura * self.altura
    
# Define a classe quadrado que herda de retangulo
class Quadrado(Retangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)  
        
        
# Define uma finção exibir área que aceira um 
# objeto forma e imprime sua área
# O método área é chamado do método forma
def exibir_area(forma):
    print(f'A área da forma é: {forma.area()}')
    
    
# Cria instâncias e círculos, retangulos e quadrados
circulo =  Circulo(5)
retangulo = Retangulo(4, 6)
quadrado = Quadrado(3)

# Chama a função exibir_área para cada instânica
# O método área  apropiado é chamado para 
# cada objeto, mostrando polimorfismo
exibir_area(circulo)
exibir_area(retangulo)
exibir_area(quadrado)