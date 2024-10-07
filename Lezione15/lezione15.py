# Esercizio 1

# Crea un context manager usando una classe

# Definisci una classe FileManager che implementa un context manager che gestisce le risorse dei file.

# Implementa appropriatamente la funzione __init__, __enter__ e la funzione  __exit__

# Esempio di funzionamento:

# Il context manager deve permettere di aprire il file, effettuare operazioni e chiudere la risorsa aperta.

# with FileManager('example.txt', 'w') as f:

#     f.write('Hello, world!')

import random

from ..Lezione19.merge import mergeSort


class FileManager:
    def __init__(self,file_name,mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file_wrapper = open(self.file_name,self.mode)
        return self.file_wrapper
    
    def __exit__(self,exc_type,exc_value,traceback):
        self.file_wrapper.close()

with FileManager(file_name="esempio.txt", mode="w") as file:
    file.write("Ciao")

# Esercizio 2

# Crea un context manager che permette di calcolare il tempo che viene impiegato ad eseguire le istruzioni che si trovano nel with

# with Timer():

#     time.sleep(1)

# time elapsed: 1.00000

# in questo esempio il tempo passato non sarà mai uguale a 1
class Timer:
    def __init__(self) -> None:
        pass

    def __enter__(self):
        import time
        self.time = time.time()

    def __exit__(self,exc_type,exc_value,traceback):
        import time 
        print(f"Time elapsed : {time.time()} - {self.time}")

lista = [random.randint(0,10000) for _ in range(1000)]
with Timer():
    mergeSort(lista)
