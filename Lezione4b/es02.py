def lenght_of_last_word(s: str) -> int:
    """
    Data una stringa s  che contiene parole e spazi. restitusce la lungezza sell'ultima parola in s.
    Una parola è una sottostringa che contiene caratteri contigui dallo spazio.
    """
    l: list[str] = s.split()
    return len(l[-1])
stringa = lenght_of_last_word(" hello   world       ")
print(stringa)