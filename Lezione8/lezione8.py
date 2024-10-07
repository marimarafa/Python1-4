class Animal:
    def __init__(self, species: str, age: int, name: str) -> None:
        self.species = species
        self.age = age
        self.name = name

    def __str__(self) -> str:
        return f'name : {self.name}, species: {self.species}, age: {self.age}'

class Cat(Animal):
    def __init__(self, species: str, age: int, name: str) -> None:
        super().__init__(species, age, name)

class Rabbit(Animal):
    def __init__(self, species: str, age: int, name: str) -> None:
        super().__init__(species, age, name)

class Person(Animal):
    def __init__(self, species: str, age: int, name: str, surname: str, cf: str) -> None:
        super().__init__(species, age, name)
        self.surname = surname
        self.cf = cf

    def __str__(self) -> str:
        return f'name = {self.name.capitalize()}, surname = {self.surname.capitalize()}, cf = {self.cf}, age = {self.age}, species: {self.species}'

class Student(Person):
    def __init__(self, species: str, age: int, name: str, surname: str, cf: str, matricula: str) -> None:
        super().__init__(species, age, name, surname, cf)
        self.matricula = matricula

# Esempi di utilizzo
persona = Person(name="marim", surname="arafa", cf="87699", age=32, species="ilu")
animale = Animal(name="Willy", species="balena", age=33)
gatto = Cat(name="Garfield", species="ksc", age=12)

print(persona)
print(animale)
print(gatto)



        


