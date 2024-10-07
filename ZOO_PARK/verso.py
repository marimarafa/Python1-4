from abc import ABC,abstractmethod

class AbcAnimal(ABC):

    
    @abstractmethod
    def verso(self):
        pass
    def movimento():
        pass

class Cane(AbcAnimal):
    def __init__(self,
                 nome :str) -> None:
        super().__init__()
    
        self.nome = nome
        self.velocità : float = 10.0 #m/S
    def verso(self):
        return ("Bau")
    
    def movimento(self,t :int):
        return self.velocità *t


class Gatto(AbcAnimal):
    def __init__(self,name) -> None:
        super().__init__()
        self.name = name
        self.velocità : float = 12.3 #m/S

    def verso(self):
        return "Miao"
    
    def movimento(self,t :int):
        return self.velocità *t
    

cane1 :Cane = Cane(nome= "Pluto")
print(cane1.verso())
print(cane1.movimento(t=10))    
gatto1:Gatto = Gatto(name="pluto")
print(gatto1.verso())
print(gatto1.movimento(t=14)) 
