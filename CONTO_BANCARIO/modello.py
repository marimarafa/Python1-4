class Banca:
    def __init__(self,nome ,simbolo) -> None:
        self.nome = nome
        self.simbolo = simbolo
        self.lista_filiali = []

    def numero_filiali(self):
        return len(self.lista_filiali)
    
    def aggiungi_filiale(self,filiale):
        return self.lista_filiali.append(filiale)
       

class Filiale:
    numero_filiali = 0

    def __init__(self,codice,indirizzo,banca:Banca) -> None:
        self.codice = codice
        self.indirizzo = indirizzo
        self.banca = banca

        Filiale.numero_filiali += 1
    
    @classmethod
    def totale_filiali_create(cls):
        return cls.numero_filiali
    
unicredit = Banca(nome="unicredit", simbolo="UCG")
intesa = Banca(nome="intesa san paolo", simbolo="ISP")

filiale1 = Filiale(codice= "UCG01",indirizzo="jjjjjjjjhpo",banca=unicredit)
filiale2 = Filiale(codice= "ISP01",indirizzo="jjjjjjjjhpo",banca=intesa)
unicredit.aggiungi_filiale(filiale1)
intesa.aggiungi_filiale(filiale2)
print(Filiale.totale_filiali_create())
print(unicredit.numero_filiali())
print(intesa.numero_filiali())




    
    

    
        