"""# Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione. L'operazione può procedere solo se la condizione A è vera o se 
# entrambe le condizioni B e C sono vere. La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.

def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA is True or (conditionB and conditionC) is True:
        return 'Operazione permessa'
    else:
        return 'Operazione negata'

print(check_combination(True, False, True))
print(check_combination(False, True, False))

#Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.

def sum_above_threshold(numbers: list[int], x:int) -> int:
    lista = []
    for num in numbers:
        if x <= num:
            lista.append(num)
            return sum(lista)

	
print(sum_above_threshold([15, 5, 25], 20))

# Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
# a) 1, 2, 3, 4, 5, 6, 7
# b) 3, 8, 13, 18, 23
# c) 20, 14, 8, 2, -4, -10
# d) 19, 27, 35, 43, 51

def print_seq(): 
    
    print("Sequenza a):")
    for num in range(1,8):
        print(num)

    print("Sequenza b):")
    for num in range(3,24,5):
        print(num)

    print("Sequenza c):")
    for num in range(20,-11,-6):
        print(num)

    print("Sequenza d):")
    for num in range(19,52,8):
        print(num)
    
print_seq()
#Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.
def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    new_dict = {}
    for key,value in prodotti.items():
        if value > 20:
            new_dict[key] = value - (value * 0.1)
    return new_dict

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0})) 

# Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
# - se x è pari, deve essere diviso per 2;
# - se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1.
def transform(x: int) -> int:
    if x % 2 == 0:
        x /= 2
    else:
        x = (x * 3) -1
    return int(x)
print(transform(5))
print(transform(-10))

#Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    dict3 = dict1.copy()
    for key, value in dict2.items():
        if key in dict3:
            dict3[key] += value
        else:
            dict3[key] = value
    return dict3

print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))

# Progettare un sistema di videonoleggio con i seguenti requisiti:

# 1. Classe Movie:

# Attributi:

# movie_id: str - Identificatore di un film.
# title: str - Titolo del film.
# director: str - Regista del film.
# is_rented: boolean - Booleano che indica se il film è noleggiato o meno.
# Metodi:

# rent(): Contrassegna il film come noleggiato se non è già noleggiato. Se il film non è già noleggiato imposta is_rented a True, altrimenti stampa il messaggio "Il film {self.title} è già noleggiato."
# return_movie(): Contrassegna il film come restituito. Se il film è già noleggiato imposta is_rented a False, altrimenti stampa il messaggio "Il film {self.title} non è attualmente noleggiato."
# 2. Classe Customer:

# Attributi:

# customer_id: str - Identificativo del cliente.
# name: str - Nome del cliente.
# rented_movies: list[Movie] - Lista dei film noleggiati.
# Metodi:

# rent_movie(movie: Movie): Aggiunge il film nella lista rented_movies se non è già stato noleggiato, altrimenti stampa il messaggio "Il film {movie.title} è già noleggiato."
# return_movie(movie: Movie): Rimuove il film dalla lista rented_movies se già presente, altrimenti stampa il messaggio "Il film {movie.title} non è stato noleggiato da questo cliente."
# 3. Classe VideoRentalStore:

# Attributi:

# movies: dict[str, Movie] - Dizionario che ha per chiave l'id del film e per valore l'oggetto Movie.
# customers: dict[str, Customer] - Dizionario che ha per chiave l'id del cliente e per valore l'oggetto Customer.
# Metodi:

# add_movie(movie_id: str, title: str, director: str): Aggiunge un nuovo film nel videonoleggio se non è già presente, altrimenti stampa il messaggio "Il film con ID {movie_id} esiste già."
# register_customer(customer_id: str, name: str): Iscrive un nuovo cliente nel videonoleggio se non è già presente, altrimenti stampa il messaggio "Il cliente con ID {customer_id} è già registrato."
# rent_movie(customer_id: str, movie_id: str): Permette al cliente di noleggiare un film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio "Cliente o film non trovato."
# return_movie(customer_id: str, movie_id: str): Permette al cliente di restituire un film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio "Cliente o film non trovato."
# get_rented_movies(customer_id: str): list[Movie] - Restituisce la lista dei film noleggiati dal client (customer.rented_movies) se il cliente esiste nel videonoleggio, altrimenti stampa il messaggio "Cliente non trovato." e ritorna una lista vuota.

class Movie:
    def __init__(self,movie_id:str,title:str,director:str) -> None:
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = False
    def rent(self):
        if self.is_rented:
            print(f"Il film {self.title} è già noleggiato.")
        else:
            self.is_rented = True
    def return_movie(self):
        if self.is_rented:
            self.is_rented = False
        else:
            print(f"Il film {self.title} non è attualmente noleggiato.")
            
class Customer:
    def __init__(self,customer_id:str,name:str) -> None:
        self.customer_id = customer_id
        self.name = name
        self.rented_movie :list[Movie]= []
    def rent_movie(self,movie:Movie):
        if  not movie.is_rented:
            movie.rent() 
            self.rented_movie.append(movie)
        else:
            print(f"Il film '{movie.title}' è già noleggiato.")
    def return_movie(self,movie:Movie):
        if movie in self.rented_movie:
            movie.return_movie()
            self.rented_movie.remove(movie)
        else:
            print(f"Il film '{movie.title}' non è stato noleggiato da questo cliente.")
class VideoRentalStore:
    def __init__(self) -> None:
        self.movies: dict[str,Movie] = {}
        self.customers: dict[str,Customer] = {}
    def add_movie(self,movie_id: str, title: str, director: str): 
        if movie_id not in self.movies.keys():
            new_movie = Movie(movie_id,title,director)
            self.movies[movie_id] = new_movie
        else:
            print(f"Il film con ID {movie_id} esiste già.")
    def register_customer(self,customer_id: str, name: str):
        if customer_id not in self.customers.keys():
            new_customer = Customer(customer_id,name)
            self.customers[customer_id] = new_customer
        else:
            print(f"Il cliente con ID {customer_id} è già registrato.")
    def rent_movie(self,customer_id: str, movie_id: str):
        if customer_id in self.customers.keys() and movie_id in self.movies.keys():
            customer = self.customers[customer_id]
            movie = self.movies[movie_id]
            customer.rent_movie(movie)
        else:
            print("Cliente o film non trovato.")
    def return_movie(self,customer_id:str,movie_id:str):
        if customer_id in self.customers.keys() and movie_id in self.movies.keys():
            customer = self.customers[customer_id]
            movie = self.movies[movie_id]
            customer.return_movie(movie)
        else:
            print("Cliente o film non trovato.")
    def get_rented_movies(self,customer_id:str)-> list[Movie]:
        if customer_id in self.customers.keys():
            customer = self.customers[customer_id]
            return customer.rented_movie
        else:
            print("Cliente non trovato")
            return []

# Creazione di un nuovo videonoleggio
videonoleggio = VideoRentalStore()

# Aggiunta di nuovi film
videonoleggio.add_movie("1", "Inception", "Christopher Nolan")
videonoleggio.add_movie("2", "The Matrix", "Wachowski Brothers")

# Registrazione di nuovi clienti
videonoleggio.register_customer("101", "Alice")
videonoleggio.register_customer("102", "Bob")

# Noleggio di film
videonoleggio.rent_movie("101", "1")
videonoleggio.rent_movie("102", "2")

# Tentativo di noleggiare un film già noleggiato
videonoleggio.rent_movie("101", "1")

# Restituzione di film
videonoleggio.return_movie("101", "1")

# Tentativo di restituire un film non noleggiato
videonoleggio.return_movie("101", "1")

# Ottenere la lista dei film noleggiati da un cliente
rented_movies_alice = videonoleggio.get_rented_movies("101")
print(f"Film noleggiati da Alice: {[movie.title for movie in rented_movies_alice]}")

rented_movies_bob = videonoleggio.get_rented_movies("102")
print(f"Film noleggiati da Bob: {[movie.title for movie in rented_movies_bob]}")

#Scrivi una funzione che prenda un dizionario e un valore, e ritorni la prima chiave che corrisponde a quel valore, o None se il valore non è presente.
def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
    for key,value in dizionario.items():
        if value == valore:
            return key
        
print(trova_chiave_per_valore({'a': 100, 'b': 200, 'c': 300}, 200))
print(trova_chiave_per_valore({'k1': 'v1', 'k2': 'v2'}, 'v3'))

#Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.
        
def classifica_numeri(lista: int) -> dict[str:list[int]]:
    lista_pari = []
    lista_dispari = []
    for num in lista:
        if num %2 == 0:
            lista_pari.append(num)
        else:
            lista_dispari.append(num)
    dizionario = {"pari": lista_pari, "dispari": lista_dispari}
    return dizionario
    
print(classifica_numeri([1, 2, 3, 4, 5, 6])) 
print(classifica_numeri([]))

#Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.
def frequency_dict(elements: list) -> dict:
    dizionario = {}
    for elem in elements:
        if elem in dizionario:
            dizionario[elem] += 1
        else:
            dizionario[elem] = 1
    return dizionario
    
print(frequency_dict(['mela', 'banana', 'mela']))

# 1. Classe Base: Veicolo
# Crea una classe base chiamata Veicolo con i seguenti attributi e metodi:
# Attributi:
# - marca (stringa)
# - modello (stringa)
# - anno (intero)
# Metodi:
# - __init__(self, marca, modello, anno): metodo costruttore che inizializza gli attributi marca, modello e anno.
# - descrivi_veicolo(self): metodo che stampa una descrizione del veicolo nel formato "Marca: [marca], Modello: [modello], Anno: [anno]".
# 2. Classe Derivata: Auto
# Crea una classe derivata chiamata Auto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
# Attributi:
# - numero_porte (intero)
# Metodi:
# - __init__(self, marca, modello, anno, numero_porte): metodo costruttore che inizializza gli attributi della classe base e numero_porte.
# - descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il - numero di porte nella descrizione, nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Numero di porte: [numero_porte]".
# 3. Classe Derivata: Moto
# Crea una classe derivata chiamata Moto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
# Attributi:
# - tipo (stringa, ad esempio "sportiva", "cruiser", ecc.)
# Metodi:
# - __init__(self, marca, modello, anno, tipo): metodo costruttore che inizializza gli attributi della classe base e tipo.
# - descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il tipo di moto nella descrizione, nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Tipo: [tipo]".
class Veicolo:
    def __init__(self,marca:str,modello:str,anno:int) -> None:
        self.marca = marca
        self.modello = modello
        self.anno = anno
    def descrivi_veicolo(self):
        print(f'Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}')
class Auto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int,num_porte:int) -> None:
        super().__init__(marca, modello, anno)
        self.num_porte = num_porte
    def descrivi_veicolo(self):
        print(f'Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.num_porte}')
class Moto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int,tipo:str) -> None:
        super().__init__(marca, modello, anno)
        self.tipo = tipo
    def descrivi_veicolo(self):
        print(f'Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}')
    
veicolo = Veicolo("Generic", "Model", 2020)
auto = Auto("Toyota", "Corolla", 2021, 4) 
moto = Moto("Yamaha", "R1", 2022, "sportiva")  
veicolo.descrivi_veicolo()  
auto.descrivi_veicolo()  
moto.descrivi_veicolo()  

#Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.
def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:
    dizionario = {}
    for i,x in tuples:
        if i in dizionario:
            dizionario[i].append(x)
        else:
            dizionario[i] = [x]
    return dizionario
                
print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))
print(lista_a_dizionario([]))

# Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, modificare, e cercare ricette basate sugli ingredienti. Il sistema dovrà essere capace di gestire una collezione (dizionario) di ricette e i loro ingredienti.

# Classe:
# - RecipeManager:
#     Gestisce tutte le operazioni legate alle ricette.

#     Metodi:
#     - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti. Restituisce un nuovo dizionario con la sola ricetta appena creata o un messaggio di errore se la ricetta esiste già.

#     - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.

#     - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

#     - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

#     - list_recipes(): Elenca tutte le ricette esistenti.

#     - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.

#     - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente. Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.
class RecipeManager:
    def __init__(self) -> None:
        self.ricette: dict[str:list[str]] = {}
    def create_recipe(self,name:str,ingredients:list[str]):
        if name in self.ricette:
            print("Ricetta già esistente.")
        else:
            self.ricette = {name:ingredients}
        return self.ricette
    def add_ingredient(self,name_recipe:str,ingredient:str):
        for value in self.ricette.values():
            if name_recipe in self.ricette:
                value.append(ingredient)
            else:
                print("Ricetta non trovata.")
        return self.ricette
    def remove_ingredient(self,name_recipe:str,ingredient:str):
        for value in self.ricette.values():
            if name_recipe in self.ricette:
                value.remove(ingredient)
            else:
                print("Ricetta non trovata.")
        return self.ricette
    
    def update_ingredient(self,recipe_name:str, old_ingredient:str, new_ingredient:str):
        if recipe_name in self.ricette:
            ingredients = self.ricette[recipe_name]
            for v in range(len(ingredients)):
                if ingredients[v] == old_ingredient:
                    ingredients[v] = new_ingredient
        return self.ricette
    
    def list_recipes(self):
        for recipe in self.ricette:
            return([recipe])
            
    def list_ingredients(self,recipe_name:str):
        if recipe_name in self.ricette:
            return self.ricette[recipe_name]
        else:
            print("Ricetta non trovata")
    def search_recipe_by_ingredient(self,ingredient:str):
        recipe ={}
        for recipes,ingredients in self.ricette.items():
            if ingredient in ingredients:
                recipe[recipes] = ingredients
                return recipe
            else:
                print("Ricetta non trovata")
                
manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.list_recipes())
print(manager.list_ingredients("Pizza Margherita"))
print(manager.search_recipe_by_ingredient("Farina"))   

# Progettare un sistema di gestione della biblioteca con i seguenti requisiti:

    # Classe Book:
        # Attributi:
            # book_id: str - Identificatore di un libro.
            # title: str - titolo del libro.
            # author: str - autore del libro
            # is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
        # Metodi:
            # borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
            # return_book()- Contrassegna il libro come restituito.

    # Classe Member:
        # Attributi:
            # member_id: str - identificativo del membro.
            # name: str - il nome del membro.
            # borrowed_books: list[Book] - lista dei libri presi in prestito.
        # Metodi:
            # borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
            # return_book(book): rimuove il libro dalla lista borrowed_books.

    # Classe Library:
        # Attributi:
            # books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
            # members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
        # Metodi:
            # add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
            # register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
            # borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
            # return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
            # get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro.
"""

class Book:
    def __init__(self,book_id:str,title:str,author:str,) -> None:
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed :bool= False
    
    def borrow(self):
        if  not self.is_borrowed:
            self.is_borrowed = True
            return False
        return True
            
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False

class Member:
    def __init__(self,member_id:str,name:str) -> None:
        self.member_id = member_id
        self.name = name
        self.borrowed_books :list[Book]= []

    def borrow_book(self,book:Book):
        if book not in self.borrowed_books and book.is_borrowed == False:
            self.borrowed_books.append(book)
            book.borrow()
        else:
            print("Book is already borrowed")
        
    def return_book(self,book:Book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
        else:
            print("Book not borrowed by this member")

class Library:
    def __init__(self) -> None:
        self.books :dict[str,Book]={}
        self.members :dict[str:Member] = {}
    
    def add_book(self,book_id: str, title: str, author: str):
        if book_id not in self.books.keys():
            book = Book(book_id,title,author)
            self.books[book_id] = book
    
    def register_member(self,member_id: str, name: str):
        if member_id not in self.members:
            member = Member(member_id,name)
            self.members[member_id] = member

    def borrow_book(self,member_id: str, book_id: str):
        if not member_id in self.members:
            print("Member not found")
        elif not book_id in self.books:
            print("Book not found")
        else:
            member:Member = self.members[member_id]
            book :Book = self.books[book_id]
            member.borrow_book(book)

    
    def return_book(self,member_id: str, book_id: str):
        if member_id in self.members and book_id in self.books:
            book:Book = self.books[book_id]
            member :Member= self.members[member_id]
            member.return_book(book)
            
    def get_borrowed_books(self,member_id:str)->list[Book]:
        lista =[]
        if member_id in self.members.keys():
            member :Member= self.members[member_id]
        for book in member.borrowed_books:
            lista.append(book.title)
        return lista
        

library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

print(library.get_borrowed_books("M001"))  # Expected output: ['The Great Gatsby']
print(library.get_borrowed_books("M002"))  #
    
    
    
# Progettare un semplice sistema bancario con i seguenti requisiti:

# Classe del Account:
# Attributi:
# account_id: str - identificatore univoco per l'account.
# balance: float - il saldo attuale del conto.
# Metodi:
# deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
# get_balance(): restituisce il saldo corrente del conto.
# Classe Bank:
# Attributi:
# accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
# Metodi:
# create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
# deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
# get_balance(account_id): restituisce il saldo del conto con l'ID specificato

class Account:
    def __init__(self,account_id:str) -> None:
        self.account_id = account_id
        self.balance :float= 0.0
        
    def deposit(self,amount:float):
        self.balance += amount
        
    def get_balance(self):
        return int(self.balance)
    
class Bank:
    def __init__(self) -> None:
        self.accounts:dict[str,Account]={}
        
    def create_account(self,account_id:str):
        if account_id not in self.accounts.keys():
            self.accounts[account_id] = Account(account_id)
        else:
            print("Account with this ID already exists")
        return self.accounts[account_id]
            
            
    def deposit(self,account_id:str,amount:float):
        if account_id in self.accounts.keys():
            self.accounts[account_id].deposit(amount)
            
    def get_balance(self,account_id:str):
        if account_id in self.accounts.keys():
            return self.accounts[account_id].get_balance()
        else:
            print("Account not found")

bank = Bank()
account1 = bank.create_account("123")
print(account1.get_balance())

bank = Bank()
account1 = bank.create_account("123")
bank.deposit("123",100)
print(bank.get_balance("123"))

bank = Bank()
account2 = bank.create_account("456")
bank.deposit("456",200)
print(bank.get_balance("456"))
        
        


