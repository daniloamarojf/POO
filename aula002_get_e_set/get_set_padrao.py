

class Minhaclasse:
    def __init__(self, valor):
        self.atributo = valor
        
    def get_atributo(self):
        return self._atributo
    
    def set_atributo(self, valor):
        self._atributo = valor
        
obj = Minhaclasse(10)
# O atributo trabalha como uma função
obj. set_atributo(20)
# Saida como função
print(obj.get_atributo())
    