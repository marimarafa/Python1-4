def anagram(s: str, t: str) -> bool:
    s = s.lower()
    t = t.lower()
    if sorted(s) == sorted(t):
        return True
    return False



    
print(anagram("anagram","nagaram"))	#True
print(anagram("rat", "car"))    #False
print(anagram("silent","listen"))   #True
print(anagram("NeurIPS","UniReps"))  #True


"""
    Classe del Account:
        Attributi:
            account_id: str - identificatore univoco per l'account.
            balance: float - il saldo attuale del conto.
        Metodi:
            deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
            get_balance(): restituisce il saldo corrente del conto.
    Classe Bank:
        Attributi:
            accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
        Metodi:
            create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
            deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
            get_balance(account_id): restituisce il saldo del conto con l'ID specificato.

"""
class Account:
    def __init__(self,
                 account_id :str,
                 balance :float) -> None:
        self.account_id = account_id
        self.balance = balance

    def deposit(self, amount :float):
        return self.balance + amount
    
    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self) -> None:
        self.accounts = {}
    def create_account(self, account_id):
        if account_id not in self.accounts:
            account1 =self.accounts[account_id] = Account(account_id=account_id,balance= 0)
            return account1
        raise ValueError("Account with this ID already exists")
    def deposit(self, account_id,amount):
        if account_id in self.accounts:
            self.accounts[account_id]= amount
    def get_balance(self,account_id):
        if account_id in self.accounts:
            return self.accounts[account_id]
        raise ValueError ("Account not found")
    
print("\n")
bank = Bank()
account1 = bank.create_account("123")
print(account1.get_balance())  #0

bank = Bank()
account1 = bank.create_account("123")
bank.deposit("123",100)
print(bank.get_balance("123"))   #100

bank = Bank()
account2 = bank.create_account("456")
bank.deposit("456",200)
print(bank.get_balance("456"))   #200

bank = Bank()
account1 = bank.create_account("123")
try:
    bank.create_account("123")
except ValueError as e:
    print(e)

bank = Bank()
try:
    bank.get_balance("456")
except ValueError as e:
    print(e)

"""
Data l'inizio di una lista concatenata, invertire la lista e restituire la lista invertita.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverse_list(head: ListNode) -> list[int]:
    lista = []
    while head is not None:
            lista.append(head.val)
            head = head.next
    lista.reverse()
    return lista

    
print("\n")
head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5)))))
print(reverse_list(head))
#[5, 4, 3, 2, 1]

head = ListNode(val=1, next=ListNode(val=2))
print(reverse_list(head))

"""Data una stringa s e una lista di stringhe wordDict, restituisce True se s può essere segmentato in una sequenza separata da spazi di una o più 
parole del dizionario; False altrimenti.
Tieni presente che la stessa parola nel dizionario può essere riutilizzata più volte nella segmentazione.
"""

def word_break(s: str, wordDict: list[str]) -> bool:
    for word in s:
        if word == wordDict[0]:
            s.replace(word,"")
    if s == wordDict[1]:
        return True
    return False



print(word_break("leetcode",["leet","code"])) #True

print(word_break("applepenapple", ["apple","pen"])) #True

print(word_break("catsandog",["cats","dog","sand","and","cat"])) #False



        
        
        

    

            








        
            






    
        


