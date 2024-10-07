# Gestione di un magazzino
# Scrivi un programma in Python che gestisca un magazzino. Il programma deve permettere di aggiungere prodotti al magazzino, cercare prodotti per nome e verificare la disponibilità di un prodotto.

# Definisci una classe Prodotto con i seguenti attributi:
# - nome (stringa)
# - quantità (intero)
 
# Definisci una classe Magazzino con i seguenti metodi:
# - aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
# - cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
# - verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
 
# Test case:
# Un gestore del magazzino crea un magazzino e diversi prodotti in diverse quantità. Successivamente, aggiunge i prodotti al magazzino.
# Il sistema cerca un prodotto per verificare se esiste nell'inventario.
# Il sistema verifica la disponibilità dei prodotti in inventario.

class Prodotto:
    def __init__(self,
                 nome:str,
                 quantità :int) -> None:
        self.nome = nome
        self.quantità = quantità
            
class Magazzino:
    def __init__(self) -> None:
        self.prodotti = []
        
    def aggiungi_prodotto(self, prodotto :Prodotto):
        self.prodotti.append(prodotto)
        return self.prodotti
    
    def cerca_prodotto(self,nome :str) -> Prodotto:
        for prodotto in self.prodotti :
            if nome == prodotto.nome:
                return prodotto
        return 'Prodotto non trovato'
    
    def verifica_disponibilità(self,nome:str) -> str:
        for prodotto in self.prodotti:
            if nome == prodotto.nome :
                return 'Prodotto disponibile'
        return 'Prodotto non disponibile'
    
prodotto1 = Prodotto(nome="Shampoo",quantità= 4)
prodotto2 = Prodotto(nome="Balsamo",quantità=5)
magazzino = Magazzino()
print(magazzino.aggiungi_prodotto(prodotto1))
print(magazzino.aggiungi_prodotto(prodotto2))
print(magazzino.cerca_prodotto("Balsamo"))
print(magazzino.cerca_prodotto("Palla a volo"))
print(magazzino.verifica_disponibilità("Shampoo"))
print(magazzino.verifica_disponibilità("carte uno"))
        
        
    
        