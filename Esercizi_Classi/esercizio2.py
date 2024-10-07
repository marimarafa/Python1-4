# Exercise 2: Implementing Static Methods
# Create a class MathOperations with a static method add that takes two numbers and returns their sum, 
# and another static method multiply that takes two numbers and returns their product.

class MathOperations:
    def __init__(self) -> None:
        pass
    @staticmethod
    def add(a:int,b:int) -> int:
        return a+b
    
    def multiply(a:int,b:int)-> int:
        return a*b 
    
print(MathOperations.add(4,10))
print(MathOperations.multiply(5,2))