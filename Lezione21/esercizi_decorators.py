#Esercizio 1 - Crea un decorator  che stampa n volte l'output della funzione decorata chiamandola due volte.
#from abc import abstractmethod
class Stampa:
    @staticmethod
    def StampaOutput(func):
        def wrapper(*args):
            func(*args)
            print(f"result is: {func(*args) }\n" * 4)
        return wrapper
    
@Stampa.StampaOutput   
def somma(a,b):
    return a+b

somma(2,3)
somma(4,6)
        
#Esercizio 2 - Crea un decorator che calcola il tempo di esecuzione della funzione che viene decorata.

class Analisi:
    @staticmethod
    def Tempo(func):
        def wrapper(*args):
            import time
            start = time.time()
            func(*args)
            print(f'Time elapsed: {time.time() - start}')
        return wrapper
    
@Analisi.Tempo
def divisione(y,x):
    return y / x

divisione(15,3)

#Esercizio 3 - Crea un decorator che permette di memorizzare informazioni sulla fibonacci in modo tale che non sia necessario ricalcolare i valori gia calcolati



