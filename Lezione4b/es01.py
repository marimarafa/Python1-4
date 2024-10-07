def is_pelindrome(x :int) -> bool:
    """  Dato un intero x,restituisce True se x è pelindromo, e False altrimenti
    Esempio1 : 
    x = 121 -> True
    Spiegazione : 121 si legge come 121 da destra che da sinistra

    Esempio2 :
    x = -121 -> False
    Spiegazione _Da sinistra a destra, leggiamoo -121, Da destra a sinistra. leggiamo 121-, Perciò,questo numero non è pelindromo

    Esempio3 :
    x = 10 -> False 
    Spiegazione : 01 da destra a sinistra, Perciò, non è palindromo
    """
    s = str(x)
    i :int = 0
    s_lenght = len(s)
    while i < (s_lenght //2 ):
        j = s_lenght - (i+1)
        if s[i] != s[j]:
            return False
        i += 1
        return True

num = is_pelindrome(22)
print(num)
