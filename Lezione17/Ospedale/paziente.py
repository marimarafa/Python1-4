
# ### CLASSE: Paziente
# Creare un file chiamato "paziente.py".
# In tale file, creare una classe chiamata Paziente. Si derivi Paziente dalla classe Persona.

# Un paziente ha un nome, un cognome, un età, definiti dalla classe Persona ed un codice identificativo (si usi il tipo String).
# - Definire i seguenti metodi:

#     costruttore della classe paziente, il quale richiede in input il codice identificativo, il quale deve essere un attributo privato.
#     setIdCode(idCode): consente di impostare il codice identificativo del paziente.
#     getidCode(): consente di ritornare il codice identificativo del paziente.
#     patientInfo(): stampa in output le informazioni del paziente in questo modo:

#         "Paziente: {nome} {cognome}
#          ID: {codice identificativo}"
from .persona import Persona

class Paziente(Persona):
    def __init__(self, first_name, last_name,id :str) -> None:
        super().__init__(first_name, last_name)
        self.__id = id
    def setIdCode(self,idCode):
        self.__id = idCode

    def getIdCode(self):
        return self.__id
    
    def patientInfo(self):
        print(f"Paziente: {self.getName()} {self.getLastName()} \nID: {self.getIdCode()}")

paziente = Paziente("mario","rossi","32355")
paziente.patientInfo()
        