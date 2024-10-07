# 1. GESTIONALE PAGAMENTO
# Si definisca una nuova classe Pagamento che contiene un attributo privato e di tipo float che memorizza l'importo del pagamento e si definiscano appropriati metodi get() e set(). L'importo non è un parametro da passare in input alla classe Pagamento ma deve essere inizializzato utilizzando il metodo set() dove opportuno. Si crei inoltre un metodo dettagliPagamento() che visualizza una frase che descrive l'importo del pagamento, ad esempio: "Importo del pagamento: €20.00". Quando viene stampato, l'importo è sempre con 2 cifre decimali.
# Successivamente, si definisca una classe PagamentoContanti che sia derivata da Pagamento e definisca l'importo. Questa classe dovrebbe ridefinire il metodo dettagliPagamento() per indicare che il pagamento è in contanti. Si definisca inoltre il metodo inPezziDa() che stampa a schermo quante banconote da 500 euro, 200 euro, 100 euro, 50 euro, 20 euro, 10 euro, 5 euro e/o in quante monete da 2 euro, 1 euro, 0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 0,01 euro sono necessarie per pagare l'importo in contanti.
# Si definisca una classe PagamentoCartaDiCredito derivata anch'essa da Pagamento e che definisce l'importo. Questa classe deve contenere gli attributi per il nome del titolare della carta, la data di scadenza, e il numero della carta di credito. Infine, si ridefinisca il metodo dettagliPagamento() per includere tutte le informazioni della carta di credito oltre all'importo del pagamento.
# Per il test, si creino almeno due oggetti di tipo PagamentoContanti e due di tipo PagamentoCartaDiCredito con valori differenti e si invochi dettagliPagamento() per ognuno di essi.
# Esempio di output:
# Pagamento in contanti di: €150.00
# 150.00 euro da pagare in contanti con:
# 1 banconota da 100 euro
# 1 banconota da 50 euro
# Pagamento in contanti di: €95.25
# 95.25 euro da pagare in contanti con:
# 1 banconota da 50 euro
# 2 banconote da 20 euro
# 1 banconota da 5 euro
# 1 moneta da 0.2 euro
# 1 moneta da 0.05 euro
# Pagamento di: €200.00 effettuato con la carta di credito
# Nome sulla carta: Mario Rossi
# Data di scadenza: 12/24
# Numero della carta: 1234567890123456
# Pagamento di: €500.00 effettuato con la carta di credito
# Nome sulla carta: Luigi Bianchi
# Data di scadenza: 01/25
# Numero della carta: 6543210987654321
from abc import abstractmethod
class Pagamento:
    def __init__(self) -> None:
        self.__importo = 0.00
    
    def setImporto(self,importo:float):
        self.__importo = importo

    def getImporto(self):
        return self.__importo
    
    def dettagliPagamento(self):
        print(f"Importo del pagamento: €{self.getImporto()}")

class PagamentoContanti(Pagamento):
    def __init__(self) -> None:
        super().__init__()
    def dettagliPagamento(self):
        print(f"Importo del pagamento: €{self.getImporto():.2f}")
    
    def inPezziDa(self):
        N = self.getImporto()
        banconote = [500, 200, 100, 50, 20, 10, 5, 2, 1, .50, .20, .10, .05, .01]
        
        for taglio in banconote: 
            if N//taglio != 0.00 and taglio >= 5 :
                print(f'{int(N//taglio)} banconota da {taglio} euro')
                N = N%taglio
            elif N//taglio != 0.00 and taglio <= 2 :
                print(f'{int(N//taglio)} moneta da {taglio} euro')
                N = N%taglio
class PagamentoCartoCredito(Pagamento):
    def __init__(self,nome:str,data_scadenza:str,numero_carta:int) -> None:
        super().__init__()
        self.nome = nome
        self.data_scadenza = data_scadenza
        self.numero_carta = numero_carta
    def dettagliPagamento(self):
        print(f'Pagamento di: {self.getImporto()} effettuato con la carta di credito \nNome sulla carta: {self.nome} \nData di scadenza: {self.data_scadenza} \nNumero della carta: {self.numero_carta}')

Pagamento()
pagamento = PagamentoContanti()
pagamento.setImporto(150.04)
pagamento.dettagliPagamento()
pagamento.inPezziDa()
pagamentocarta = PagamentoCartoCredito(nome="mario rossi",data_scadenza="23/34",numero_carta=2122932523485)
pagamentocarta.setImporto(200.0)
pagamentocarta.dettagliPagamento()


# 2. RENDERING GRAFICO
# Si vuole sviluppare un sistema in Python per gestire il rendering di diverse forme geometriche. Il sistema dovrà supportare almeno tre tipi di forme: quadrati, rettangoli, e triangoli rettangoli.

# Definire la classe astratta Forma che sarà utilizzata per definire l'attributo corrispondente al nome della forma e le funzionalità base di ogni forma, come i metodi astratti getArea() per calcolare l'area e render() per disegnare su schermo la forma.

# Definire la classe Quadrato che estende la classe Forma e aggiunge specifiche circa la lunghezza di un suo lato.
# Il costruttore della classe deve ricevere come argomento solo il lato del quadrato, ed impostare il nome della forma su "Quadrato".
# Il metodo getArea() deve calcolare l'area del quadrato.
# Il metodo render() deve stamapre su schermo un quadrato avente lato pari al valore passato nel costruttore. Il quadrato da stampare deve essere un quadrato vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)

# Definire la classe Rettangolo che estende la classe Forma e aggiunge specifiche circa la lunghezza della sua base e della sua altezza.
# Il costruttore della classe deve ricevere come argomento solo la base e l'altezza del rettangolo, ed impostare il nome della forma su "Rettangolo".
# Il metodo getArea() deve calcolare l'area del rettangolo.
# Il metodo render() deve stampare su schermo un rettangolo avente base ed altezza pari ai valori passati nel costruttore. Il rettangolo da stampare deve essere un rettangolo vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)

# Definire la classe Triangolo che estende la classe Forma e aggiunge specifiche circa la dimensione di un lato del triangolo (per semplicità, si suppone che il triangolo in questione sia un triangolo rettangolo).
# Il costruttore della classe deve ricevere come argomento solo il lato del triangolo, ed impostare il nome della forma su "Triangolo".
# Il metodo getArea() deve calcolare l'area del triangolo.
# Il metodo render() deve stampare su schermo un triangolo rettangolo avente i due cateti di lunghezza pari ai valori passati nel costruttore. Il triangolo da stampare deve essere un triangolo vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)
 
# Hint: per il disegno utilizzare print("*", end=" "), dato che l'argomento end = " " permette di controllare come termina ogni chiamata a print, e impostandolo a uno spazio si può fare in modo che tutte le stampe successive siano sulla stessa riga, separate da uno spazio.

# Esempi di output:
# Ecco un Quadrato di lato 4!

# * * * *
# *      *
# *      *
# * * * *
# L'area di questo quadrato vale: 16

# Ecco un Rettangolo avente base 8 ed altezza 4!
# * * * * * * * *
# *                *
# *                *
# * * * * * * * *
# L'area di questo rettangolo vale: 32

# Ecco un Triangolo avente base 4 ed altezza 4!
# *      
# * *    
# *   *  
# * * * *
# L'area di questo triangolo vale: 8.0
print("\n")
class Forma:
    def __init__(self,nome) -> None:
        self.nome = nome
    @abstractmethod
    def getArea(self):
        pass
    def render(self):
        pass
class Quadrato(Forma):
    def __init__(self,lunghezza:int) -> None:
        super().__init__("Quadrato")
        self.lunghezza = lunghezza
    def getArea(self):
        return f'L area di questo quadrato vale:{ self.lunghezza **2}'
    def render(self):
        print(f"Ecco un {self.nome} di lato {self.lunghezza}!")
        print( "*" *(self.lunghezza))
        for _ in range(self.lunghezza -2):
            print("*" + (" " * (self.lunghezza - 2)) + "*") 
        print( "*" *(self.lunghezza))

class Rettangolo(Forma):
    def __init__(self,len_base :int,len_alt:int) -> None:
        super().__init__( "Rettangolo")
        self.base = len_base
        self.alt = len_alt
    def getArea(self):
        return f'L area di questo rettangolo vale:{self.base *self.alt}'
    def render(self):
        print(f'Ecco un {self.nome} avente base {self.base} ed altezza {self.alt}!')
        print("*" * self.base)
        for _ in range(self.alt-2):
            print("*" + " " * (self.base - 2) + "*")
        print("*" * self.base)
class Triangolo(Forma):
    def __init__(self,lato:int) -> None:
        super().__init__("Triangolo")
        self.lato = lato
    def getArea(self):
        return  f'L area di questo triangolo vale:{(self.lato **2 )/2}'
    def render(self):
        print(f"Ecco un {self.nome} avente base e altezza {self.lato}!")
        for i in range(self.lato):
            for _ in range(i+1):
                print("*" , end=" ")
                i += 1
            print()
            
quad = Quadrato(lunghezza=5)
print(quad.getArea())
quad.render()
rettan = Rettangolo(len_base=10,len_alt=4)
print(rettan.getArea())
rettan.render()
triangolo = Triangolo(lato=4)
print(triangolo.getArea())
triangolo.render()
    

