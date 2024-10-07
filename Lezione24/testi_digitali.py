class Documento:
    def __init__(self,testo:str) -> None:
        self.testo = testo
    
    def getText(self):
        return self.testo
    
    def setText(self,testo):
        self.testo = testo

    def IsInText(self,word):
        if word in self.testo:
            return True
        return False
    
class Email(Documento):
    def __init__(self, testo: str,mittente:str,destinatario:str,titolo_mess:str) -> None:
        super().__init__(testo)
        self.mittente = mittente
        self.destinatario = destinatario
        self.titolo_mess = titolo_mess
    
    def getMit(self):
        return self.mittente
    
    def getDes(self):
        return self.destinatario
    
    def getTitMess(self):
        return self.titolo_mess
    
    def setDes(self,des):
        self.destinatario = des

    def setMit(self,mitt):
        self.mittente = mitt
    
    def setTitMess(self,titolo_mess):
        self.titolo_mess = titolo_mess
    
    def getText(self):
        return f'Da:{self.getMit()},A:{self.getDes()} \nTitolo:{self.getTitMess()} \nMessaggio:{self.testo}'
    
   
class File(Documento):
    def __init__(self, testo: str,percorso) -> None:
        super().__init__(testo)
        self.percorso = f'Lezione24/{percorso}'
    
    def getText(self):
        return f'Percorso:{self.percorso} \nContenuto:Questo e il contenuto del file:\n{email.getText()}.' 
    
email = Email(mittente="bob12@gmail.com",destinatario="alice3@gmail.com",testo="Buongiorno alice come stai?",titolo_mess="Buongiorno")
file1 = File(testo=email.getText(), percorso= "document.txt")

def LeggiTestoDaFile():
    with open(file1.percorso, "w") as file:
        file.write(email.getText())
LeggiTestoDaFile()


