from abc import ABC,abstractmethod


class Volo(ABC):
    def __init__(self,codice_volo:str,pos_disponibili:int) -> None:
        self.codice_volo = codice_volo
        self.pos_disponibili = pos_disponibili
        self.prenotazioni = 0

    @abstractmethod
    def prenota_posti(self):
        pass
    def posti_disponibili(self):
        pass
class VoloCommerciale(Volo):
    def __init__(self, codice_volo, pos_disponibili) -> None:
        super().__init__(codice_volo, pos_disponibili)
        self.eco_prenotati = 0
        self.bus_prenotati = 0
        self.prim_prenotati = 0

        self.pren_economica = int(self.pos_disponibili * 0.7)
        self.pren_business = int(self.pos_disponibili * 0.2)
        self.pren_prima = self.pos_disponibili -(self.pren_business + self.pren_economica)

    def prenota_posti(self,posti:int,classe_servizio: str):
        if self.posti_disponibili()['posti disponibili'] > posti:
            if classe_servizio == "economica" and self.posti_disponibili()['classe economica'] > posti:
                self.eco_prenotati += posti
                print(f"{posti} posti prenotati nella classe economica.Codice volo :{self.codice_volo}.")
            elif classe_servizio == "business" and self.posti_disponibili()["classe business"] > posti:
                self.bus_prenotati += posti
                print(f"{posti} posti prenotati nella classe business.Codice volo :{self.codice_volo}.")
            elif classe_servizio == "prima" and self.posti_disponibili()["classe prima"] > posti:
                self.prim_prenotati += posti
                print(f"{posti} posti prenotati nella classe prima.Codice volo :{self.codice_volo}.")
            else:
                print("Classe non valida")
        else:
            print("Non ci sono posti disponibili")

        self.prenotazioni = self.eco_prenotati + self.bus_prenotati + self.prim_prenotati
            
    def posti_disponibili(self):
        disponibili=self.pos_disponibili - self.prenotazioni
        economica_disp = self.pren_economica - self.eco_prenotati
        business_disp = self.pren_business - self.bus_prenotati
        prima_disp = self.pren_prima - self.prim_prenotati
        if disponibili <= 0 :
            disponibili = 0
        if economica_disp <= 0:
            economica_disp = 0
        if business_disp <= 0:
            business_disp = 0
        if prima_disp <= 0:
            prima_disp = 0

        available_seats = {"posti disponibili" :disponibili,"classe economica": economica_disp,"classe business": business_disp,"classe prima":prima_disp}
        return available_seats

class VoloCharter(Volo):
    def __init__(self, codice_volo, pos_disponibili,costo_volo:float) -> None:
        super().__init__(codice_volo, pos_disponibili)
        self.costo_volo = costo_volo
    def prenota_posti(self,num_posti):
        if self.posti_disponibili() >= num_posti:
            print(f"il volo charter {self.codice_volo} è stato prenotato completamente.Prezzo pagato :{self.costo_volo * num_posti}")
        else:
            print("Volo charter già prenotato..")

    def posti_disponibili(self):
        return self.pos_disponibili
    
class CompagniaAerea:
    def __init__(self) -> None:
        self.nome :str = input("Scrivi il nome della compagnia:")     
        self.costo :float = input("Prezzo standard del biglietto:")   
        self.flotta = []
    def aggiungi_volo(self,volo_commerciale:VoloCommerciale):
        self.flotta.append(volo_commerciale)

    def rimuovi_volo(self,volo_commerciale:VoloCommerciale):
        self.flotta.remove(volo_commerciale)

    def mostra_flotta(self):
        for volo in self.flotta:
            print(f'Volo {self.nome} , codice volo {volo.codice_volo}')

    def guadagno(self):
        for volo in self.flotta:
            guadagno_eco = self.costo * volo.eco_prenotati
            guadagno_bus = (self.costo ** 2) * volo.bus_prenotati
            guadagno_prima = (self.costo ** 3 ) * volo.prim_prenotati

        return f'Guadagno: {guadagno_eco +guadagno_bus + guadagno_prima}'

volo_comm = VoloCommerciale(codice_volo= "345f", pos_disponibili= 300)
volo_comm.prenota_posti(posti=14,classe_servizio= "economica")
print(volo_comm.posti_disponibili())   
volo_comm.prenota_posti(posti=9,classe_servizio= "business")
print(volo_comm.posti_disponibili())
voloc = VoloCharter(codice_volo="jh766",pos_disponibili=400,costo_volo=340.00)
voloc.prenota_posti(300)
print(voloc.posti_disponibili())
comp_aerea = CompagniaAerea()
comp_aerea.aggiungi_volo(volo_comm)
comp_aerea.mostra_flotta()
print(comp_aerea.guadagno)






    