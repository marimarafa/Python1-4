#from ..Lezione11.cinema import Film
# Catalogo Film 
# Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere, rimuovere e cercare film di un particolare regista. Il sistema dovrebbe consentire anche di visualizzare tutti i registi e i loro film.

# Classe:
# - MovieCatalog: Gestisce tutte le operazioni legate al catalogo dei film.

#     Metodi:
#     - add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo. Se il regista non esiste, viene creato un nuovo record. Se il regista esiste, la sua lista di film viene aggiornata.

#     - remove_movie(director_name, movie_name): Rimuove un film specifico dall'elenco dei film di un regista. Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.

#     - list_directors(): Elenca tutti i registi presenti nel catalogo.

#     - get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.

#     - search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo. Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata o un messaggio di errore se nessun film contiene la parola cercata nel titolo.

class MovieCatalog:
    def __init__(self):
        self.catalog = {}

    def add_movie(self,director_name,movies):
        if director_name not in self.catalog:
            self.catalog[director_name] = []
            self.catalog[director_name].append(movies)
        
    def remove_movie(self, director_name, movie_name):
        if director_name in self.catalog:
            if movie_name in self.catalog[director_name]:
                self.catalog[director_name].remove(movie_name)
                if not self.catalog[director_name]:
                    del self.catalog[director_name]
                    

    def list_directors(self):
        # for directors in self.catalog:
        #     print(directors)
        return f'Registi nel catalogo: {list(self.catalog.keys())}'
    
    def get_movies_by_director(self,director_name):
        return (f'"Film di {director_name}:", {self.catalog[director_name]} ')
    
    def search_movies_by_title(self,title):
        result = {}

        for director, movies in self.catalog.items():
            matching_movies = []
            
            for movie in movies:                   
                if title in movie:
                    matching_movies.append(movie)
                    
            if matching_movies:
                    result[director] = matching_movies
                    
        if result:
            return result
        else:
            return "Nessun film trovato"
                



catalog = MovieCatalog()
(catalog.add_movie("Christopher Nolan", ["Inception", "Interstellar", "Dunkirk"]))
(catalog.add_movie("Quentin Tarantino", ["Pulp Fiction", "Kill Bill", "Django Unchained"]))
(catalog.remove_movie("Quentin Tarantino", "Kill Bill"))
print(catalog.list_directors())
print(catalog.get_movies_by_director("Quentin Tarantino"))
print(catalog.search_movies_by_title("Inception"))
print(catalog.search_movies_by_title("Matrix"))
                    
        