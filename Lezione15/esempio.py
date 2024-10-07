#reader = (open("Lezione15/esempio.txt"))
with open("Lezione15/esempio.txt") as reader:
    print(reader)


try:
    reader.readline()
    print("sono nella try")
    raise Exception("Eccezione!")

except Exception:
    print("sono nella except")

finally:
    print("sono nella finaly")
    reader.close()

class ContextManager:
    def __enter__(self):
        print("ciao sono nell enter")
        return self
    
    def __exit__(self,exc_type,exc_value,traceback):
        if exc_type is not None:

            print("Exception")

        return False

with ContextManager() as cm:
    print("Ciao")