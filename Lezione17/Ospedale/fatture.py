# ### CLASSE: Fattura
# Creare un file chiamato "fatture.py".
# In tale file, creare una classe chiamata Fattura.

# - Definire i seguenti metodi:

#     init(patient,doctor): deve avere come input una lista di pazienti ed un dottore. Tale metodo deve verificare se il dottore può esercitare la professione, richiamando la funzione isAValidDoctor(). In caso affermativo assegnare all'attributo fatture (di tipo intero) il numero di pazienti che ha il dottore, mentre assegnare 0 all'attributo salary (di tipo int).  In caso contrario, assegnare il valore None a tutti i 4 gli attributi della classe e stampare un messaggio di errore, come, ad esempio: "Non è possibile creare la classe fattura poichè il dottore non è valido!".
#     getSalary(): deve ritornare il salario guadagnato dal dottore. Il salario gudaganto viene calcolato moltiplicando la parcella del dottore per il numero di pazienti.
#     getFatture(): deve assegnare all'attributo fatture il numero di pazienti (in modo che sia sempre aggiornato) che ha il dottore e ritornare il suo valore.
#     addPatient(newPatient): consente di aggiungere un paziente alla lista di pazienti di un dottore, aggiornando poi il numero di fatture ed il salario, richiamando il metodo getFatture() e getSalary().  Stampare "Alla lista del Dottor cognome è stato aggiunto il paziente {codice_identificativo}"
#     removePatient(idCode): consente di rimuovere un paziente alla lista di pazienti di un dottore ricevendo in input il codice identificativo del paziente da rimuovere, aggiornando poi il numero di fatture e il salario, richiamando il metodo get Fatture() e getSalary(). Stampare "Alla lista del Dottor cognome è stato rimosso il paziente {codice_identificativo}".
from .dottore import Dottore
from .paziente import Paziente

class Fattura:
    def __init__(self,patient: list[Paziente], doctor:Dottore) -> None:
        self.__patient :list[Paziente]= patient
        self.__doctor = doctor
        if self.__doctor.isAValidDoctor():
            self.__salary :int = 0
            self.__fatture :int = len(self.__patient)
        else:
            self.__doctor = None
            self.__patient = None
            self.__salary = None
            self.__fatture = None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")

    def getSalary(self):
        self.__salary = self.__doctor.getParcel() * self.__fatture
        return self.__salary
    
    def getFatture(self):
        return self.__fatture
    
    def getPatient(self):
        return self.__patient
    
    def addPatient(self,newPatient:Paziente):
        self.__patient.append(newPatient)
        self.getSalary()
        self.getFatture()
        print(f"Alla lista del Dottor {self.__doctor.getLastName()} è stato aggiunto il paziente {newPatient.__id}")

    def removePatient(self,idCode:str):
        for paziente in self.__patient:
            if idCode == paziente.__id:
                self.__patient.remove(paziente)
                self.getSalary()
                self.getFatture()
                print(f"Alla lista del Dottor {self.__doctor.getLastName()} è stato rimosso il paziente {paziente.__id}")

doctor = Dottore("Mario","Rossi","dentista",12.5)
doctor.setAge(45)
paziente = Paziente("mario","rossi","VSEW55")
paziente1 = Paziente("marVEVZASEWo","rcesi","32rvr55")
paziente2 = Paziente("eassssssfgwe","recwei","EVCCV55vecsWE")
fattura = Fattura([paziente, paziente1, paziente2], doctor)

print(fattura.getSalary())
print(fattura.getFatture())
print(fattura.getPatient())



        