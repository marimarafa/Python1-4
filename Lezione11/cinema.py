# Sistema di Prenotazione Cinema

# Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. Il cinema ha diverse sale, ognuna con un diverso film in programmazione. Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.
 
# Classi:
# - Film: Rappresenta un film con titolo e durata.
 
# - Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.

# Metodi:
#     - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di conferma o di errore.
#     - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
 
# - Cinema: Gestisce le operazioni legate alla gestione delle sale.

# Metodi:
#     - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
#     - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.

# Test case:

#     Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
#     Un cliente sceglie un film e prenota un certo numero di posti.
#     Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.

class Film:
    def __init__(self, titolo: str, durata: float) -> None:
        self.titolo = titolo
        self.durata = durata

class Sala:
    def __init__(self, numero_id: int, film: Film, tot_posti: int) -> None:
        self.numero_id = numero_id
        self.film = film
        self.tot_posti = tot_posti
        self.posti_prenotati = 0

    def prenota_posti(self, num_posti: int) -> str:
        if num_posti <= self.posti_disponibili():
            self.posti_prenotati += num_posti
            return 'Posti prenotati con successo'
        else:
            return 'Errore, posti non disponibili'

    def posti_disponibili(self) -> int:
        return self.tot_posti - self.posti_prenotati

class Cinema:
    def __init__(self) -> None:
        self.sale = []

    def aggiungi_sala(self, sala: Sala) -> None:
        self.sale.append(sala)
        return self.sale

    def prenota_film(self, titolo_film: str, num_posti: int) -> str:
        for sala in self.sale:
            if sala.film.titolo == titolo_film:
                if num_posti <= sala.posti_disponibili():
                    sala.prenota_posti(num_posti)
                    return f'{num_posti} posti prenotati per il film {titolo_film}'
                else:
                    return f'Posti non disponibili per il film {titolo_film}'
        return f'Film non disponibile'


film1 = Film(titolo="Spiderman", durata=1.50)
film2 = Film(titolo="Peter Pan", durata=2.0)
sala1 = Sala(numero_id=134, film=film1, tot_posti=40)
sala2 = Sala(numero_id=124, film=film2, tot_posti=50)
cinema = Cinema()
cinema.aggiungi_sala(sala1)
cinema.aggiungi_sala(sala2)
print(sala1.prenota_posti(5))  
print(sala1.prenota_posti(50))  
print(sala2.prenota_posti(10))  
print("Posti disponibili:", sala1.posti_disponibili())  
print("Posti disponibili:", sala2.posti_disponibili())  
print(cinema.prenota_film("Spiderman", 3))  
print(cinema.prenota_film("Peter Pan", 5))  
print(cinema.prenota_film("Spiderman", 500))  
print(cinema.prenota_film("Beaty and the beast", 5)) 