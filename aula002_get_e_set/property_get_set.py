

class Minhaclasse:
    def __init__(self, valor):
        self.atributo = valor
        
    @property
    def atributo(self):
        return self._atributo
        
    @atributo.setter
    def atributo(self, valor):
        self._atributo = valor
        
obj = Minhaclasse(10)
# O atributo trabalha como uma variável
obj.atributo = 20 #(set)        
# said semelhante a uma variável
print(obj.atributo) # (get)         