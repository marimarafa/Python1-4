def ciao(name):
    return f'Ciao {name}'

def saluta_bob(func):
    return func("Bob")

print(saluta_bob(ciao))

def parent():
    print("sono in parent")

    def first_child():
        print("sono in first child")

    return first_child

parent()

def decorator(func):
    def wrapper(*args):
        import time

        start = time.time()
        func(*args)
        print(f"Time elapsed: {time.time() - start}")
        
    return wrapper

def ciao():
    print("Ciao !")
ciao = decorator(ciao)
ciao()

