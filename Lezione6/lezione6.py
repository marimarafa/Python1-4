class Persona:
    def __init__(self,name:str,
                 surname:str,
                 date_of_birth:str,
                 genere:str,
                 codice_fiscale :str) -> None:
        
        self.name:str = name
        self.surname :str = surname
        self.date_of_birth:str = date_of_birth
        self.genere :str = genere
        self.codice_fiscale = codice_fiscale
    
    def calcola_età(self) -> int:
        return 10
    
    def __eq__(self, value: object) -> bool:
        return value.codice_fiscale == self.codice_fiscale


person_1 :Persona = Persona(name= "marim",
                            surname="arafa",
                            date_of_birth="25/11/2004",
                            genere= "Femmina")
class Dipendente(Persona):
    def __init__(self,
                name: str,
                surname: str,
                date_of_birth: str,
                genere: str,
                ore_lavorate:int) -> None:
        
        super().__init__(name, surname, date_of_birth, genere)
        self.ore_lavorate = ore_lavorate

    def calcola_stipendio(self) -> float:
        return 500.0
    
    def __eq__(self, value: object) -> bool:
        return super().__eq__(value)


dipendente_1 :Dipendente = Dipendente(name= "marim",
                            surname="arafa",
                            date_of_birth="25/11/2004",
                            genere= "Femmina",
                            ore_lavorate= 500)

class Professore(Dipendente):
    def __init__(self,
                name: str,
                surname: str,
                date_of_birth: str,
                genere: str,
                ore_lavorate: int,
                materia_inserita :str,
                ore_di_lezione :int) -> None:
        
        super().__init__(name, surname, date_of_birth, genere, ore_lavorate)
        self.materia_inserita = materia_inserita
        self.ore_di_lezione = ore_di_lezione

    def __str__(self) -> str:
        return super().__str__()
    
    def __eq__(self, value: object) -> bool:
        return super().__eq__(value)

professore_1 :Professore = Professore(name= "marim",
                            surname="arafa",
                            date_of_birth="25/11/2004",
                            genere= "Femmina",
                            ore_lavorate= 500,
                            materia_inserita = "Python",
                            ore_di_lezione = 400)


print(person_1.calcola_età())
print(dipendente_1.name)
print(dipendente_1.calcola_stipendio())
print(dipendente_1.ore_lavorate)
print(professore_1.ore_di_lezione)