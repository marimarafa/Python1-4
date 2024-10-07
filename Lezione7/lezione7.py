#marim arafa
#10-05-2024
"""
Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario.
Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.
"""
def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:
    dict = {}
    for key, value in tuples:
        if key in dict:
            dict[key].append(value)
        else:
            dict[key] = [value]
    return dict

print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))
print(lista_a_dizionario([]))
print("\n")

"""
Scrivi una funzione che inverte le chiavi e i valori in un dizionario. Se ci sono valori duplicati,
scarta i duplicati.
"""
def inverti_mappa(dizionario: dict[str:int]) -> dict[int:str]:
    dict = {}
    for keys,values in dizionario.items():
       if values not in dict:
            dict[values] = keys
    return dict

print(inverti_mappa({'a': 1, 'b': 2, 'c': 3}))
print("\n")

"""
Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega 
i voti per studente in un nuovo dizionario.
"""
def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    dict = {}
    for i in voti:
        nome = i['nome']
        voto = i['voto']
        if nome in dict:
            dict[nome].append(voto)
        else:
            dict[nome] = [voto]
    return dict
                        
print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))
print("\n")

"""
Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. Il dizionario contiene elementi
da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.
"""
def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    for keys,values in da_rimuovere.items():
        for _ in range(values):
            if keys in lista:
                lista.remove(keys)
    return lista

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
print(rimuovi_elementi([], {2: 1})) 
print("\n")

"""
Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un
prezzo superiore a 20, scontati del 10%.
"""
def filtra_e_mappa(prodotti: dict[str:float]) -> list[str:float]:
    prodotti_scontati = {}
    for keys, values in prodotti.items():
        if values > 20:
            prezzo_scontato = values - (values * 0.1)
            prodotti_scontati[keys] = prezzo_scontato
    return prodotti_scontati
    
print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0}))    
print("\n")      