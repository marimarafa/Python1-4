# Sistema di Gestione Biblioteca
# Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi. Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli, restituirli e visualizzare quali libri sono disponibili in un dato momento.
# Classi:
# - Libro: Rappresenta un libro con titolo, autore, stato del prestito. Il libro deve essere inizialmente disponibile (non prestato).
# - Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.
#     Metodi:
#     - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. Restituisce un messaggio di conferma.

#     - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile. Restituisce un messaggio di stato.

#     - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. Restituisce un messaggio di stato.

#     - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. Se non ci sono libri disponibili, restituisce un messaggio di errore.
# Test Cases:
# - Un amministratore della biblioteca aggiunge alcuni libri all'inventario.
# - Un utente prende in prestito un libro, che viene quindi marcato come non disponibile.
# - L'utente restituisce il libro, che viene marcato di nuovo come disponibile.
# - In qualsiasi momento, un utente può visualizzare quali libri sono disponibili per il prestito.

class Libro:
    def __init__(self,
                 titolo :str,
                 autore:str ) -> None:
        self.titolo = titolo
        self.autore = autore
        self.stato_del_prestito = True
    
class Biblioteca:
    def __init__(self) -> None:
        self.libri = []

    def aggiungi_libro(self,libro:Libro):
        self.libri.append(libro)
        return f'Libro {libro.titolo} aggiunto alla biblioteca'
    
    def presti_libro(self,titolo:str):
        for libro in self.libri:
            if libro.titolo == titolo:
                if libro.stato_del_prestito:
                    return f'Libro {libro.titolo} disponibile,puo essere prestato'
                libro.stato_del_prestito = False
        return 'Libro non disponibile'
    
    def restituisci_libro(self,titolo:str):
        for libro in self.libri:
            if libro.titolo == titolo:
                if libro.stato_del_prestito == False:
                    libro.stato_del_prestito == True
                return f'libro {titolo} restituito'
        return 'Libro non prestato'
    
    def mostra_libri(self):
        for libro in self.libri:
            if libro.stato_del_prestito:
                return f'Libri disponibili : {self.libri}'
        else:
            return 'Nessun libro disponibile'
        
libro1 = Libro(titolo= "La caccia al tesoro",autore="Giuseppe Rossi")
libro2 = Libro(titolo="Python",autore="Giorgio Rossi")
biblioteca = Biblioteca()
print(biblioteca.aggiungi_libro(libro1))
print(biblioteca.aggiungi_libro(libro2))
print(biblioteca.presti_libro("La caccia al tesoro"))
print(biblioteca.presti_libro("NNNjcocw"))
print(biblioteca.presti_libro("Python"))
print(biblioteca.restituisci_libro("Python"))
print(biblioteca.restituisci_libro("La caccia al tesoro"))
print(biblioteca.restituisci_libro("Pythonssskml"))
print(biblioteca.mostra_libri())