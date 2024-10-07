"""
ex.1  Let’s try to define a function named subtract ourselves:
 Personal Message: Use a variable to represent a person’s name, and print a message
- It should take 2 parameters.
to that person. Your message should be simple, such as, “Hello Eric, would you like to
- Inside the function, it should subtract the two.
learn some Python today?”
- Then, return the result.
"""
#questa variabile contiene il nome 
"""
"""
def subtract(a,b):
    return a -b
a,b = (10,6)
sottrazione = subtract(a,b)
print(f'Il risultato di {a} - {b} è: {sottrazione}')

"""

ex.2  Write a function check_value(), which takes a number as an argument.
Using if / else, the function should print whether the number is bigger, smaller,
or equal to 5.
"""
def check_value(n):
    if n > 5:
        print(f'Il numero {n} è più grande di 5')
    elif n == 5:
        print(f'Il numero {n} è uguale a 5')
    else:
        print(f'Il numero {n} è più piccolo di 5')

check_value(3)

"""
ex.3  Write a function check_length(), which takes a string as an argument.
Using if / else, check if the length of the string is bigger, smaller, or equal to 10
characters.
"""
def check_lenght(a):
    if len(a) > 10:
        print(f'la lunghezza di {a} è {len(a)} più lunga di 10')
    elif len(a) == 10:
        print(f'la lunghezza di {a} è  {len(a)} uguale a 10')
    else:
        print(f'la lunghezza di {a} è {len(a)} più corta di 10')

check_lenght("ciao")

"""
ex.4  Write a function print_numbers(), which takes a list of numbers as argument.
Using a for loop, print each number one by one.
"""
def Print_numbers(lista):
    for e in lista:
        print(e)

Print_numbers([2,54,76.5])


"""
ex.5  Write a function check_each(), which takes a list of numbers as argument.
Using a for loop, iterate through the list.
For each number, print “bigger” if it’s bigger than 5, “smaller” if it’s smaller than 5,
and “equal” if it’s equal to 5.
"""
def check_each(lista):
    for e in lista:
        ris = check_value(e)
    return ris
print(check_each([4,5,6,34.53]))


"""
ex.6  Exercise 5
Write a function add_one(). It takes an integer as argument. The function adds 1 to
the integer and returns it.
Write another function add_one_to_list(). It takes a list of integers as argument.
Define a variable new_list in this function.
Using a for loop, iterate through the argument list.
Using add_one(), fill new_list with integers from the argument list incremented
by 1.
Print new_list.
Example:
add_one_to_list([1, 2, 3])-> [2, 3, 4]
"""
def add_one(n):
    n = n+1 
    return n
def add_one_to_list(lista):
    new_list = []
    for e in lista:
        a = add_one(e)
        new_list.append(a)
    return new_list

print(add_one_to_list([2,3,5,6,7,8]))