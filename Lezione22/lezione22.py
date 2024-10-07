
class Analisi:

    @staticmethod
    def tempo(func):
        def wrapper(*args):
            import time
            start = time.time()
            func(*args)
            print(f"Time elapsed: {time.time() - start}")
        return wrapper

@Analisi.tempo
def area_cerchio(raggio:float):
    return raggio * raggio * 3.14

area_cerchio(1)


def generatore():
    yield "A"
    yield "B"
    yield "C"

prove_generatore = generatore()
print(next(prove_generatore))
print(next(prove_generatore))
print(next(prove_generatore))

from contextlib import contextmanager
import time

@contextmanager
def context_manager_decorator(*args):
    start_time :float = time.time()
    yield
    end_time :float = time.time()
    elapsed_time = end_time - start_time

    print(f'Elaspsed time: {elapsed_time}')

@context_manager_decorator
def area_cerchio(raggio:float):
    return raggio * raggio * 3.14

area_cerchio(1)

import sys
a = []
b = a 
print(sys.getrefcount(a))
print(sys.getrefcount(b))

threads :list = []
def thread_function(name):
    print(f'{name} Time - {time.time()}')
    time.sleep(2)
    print(f'{name} Time - {time.time()}')

import threading

print(f'Prima di thread')
for i in range(3):
    x = threading.Thread(target= thread_function, args= (i, ))
    threads.append(x)
    x.start()
print(f'Thread parito ')

for t in threads:
    t.join()
print("Thread finito ?????")