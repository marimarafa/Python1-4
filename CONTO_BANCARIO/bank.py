from typing import Any


class ContoBancario():
    
    total_accounts = 0
    def __init__(self,iban,saldo,nome) :
        self.iban = iban
        self.saldo = saldo
        self.nome = nome

        ContoBancario.total_accounts += 1

    def deposito(self,importo):
        self.saldo += importo
        print(f'{importo} depositato. Il nuovo saldo è {self.saldo}')

    def prelievo(self,importo):
        self.saldo += importo
        print(f'{importo} depositato. Il nuovo saldo è {self.saldo}')
    
    @classmethod
    def get_total_accounts(cls):
        print(f'Account totali creati: {cls.total_accounts}')
    
    @staticmethod
    def valida_accounts(iban:Any):
        if isinstance(iban, int) and len(str(iban)) == 10:
            print("iban valido")
            return True
        else:
            print("iban non valido")
            return False
        
account1 = ContoBancario(1234069790,0,"Alice")
account2 = ContoBancario(9876459035,1000,"Bob")

account1.deposito(500)
account1.prelievo(200)

account2.deposito(200)
account2.prelievo(150)

ContoBancario.get_total_accounts()

account3 = ContoBancario(1234065650,0,"Alice")
ContoBancario.get_total_accounts()

ContoBancario.valida_accounts(1235780)
ContoBancario.valida_accounts("1234596Abc")





        