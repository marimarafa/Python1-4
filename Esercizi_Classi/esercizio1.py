# Exercise 1: Creating an Abstract Class with Abstract Methods
# Create an abstract class Shape with an abstract method area and another abstract method perimeter. Then, create two subclasses Circle and
# Rectangle that implement the area and perimeter methods.

from abc import abstractmethod
import math

class Shape:
    def __init__(self) -> None:
        pass
    @abstractmethod
    def area(self) -> float:
        pass
  
    def perimeter(self) -> float:
        pass

class Circle(Shape):
    def __init__(self,
                 radius:int) -> None:
        super().__init__()
        self.radius = radius
        
    def area(self) -> float:
        return math.pi * (self.radius ** 2)
    
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
    
class Rectangle(Shape):
    def __init__(self,
                 lenght:int,
                 width:int) -> None:
        super().__init__()
        self.length = lenght
        self.width = width
        
    def area(self) -> int:
        return self.length * self.width

    def perimeter(self) -> int:
        return 2 * (self.length + self.width)
    
circle = Circle(radius= 4)
rectangle  = Rectangle(lenght= 5, width= 6)
print(f'Area of the circle: {circle.area()}.\nPerimeter: {circle.perimeter()}')
print(f'Area of the rectangle: {rectangle.area()}.\nPerimeter: {rectangle.perimeter()}')

    
    
        
        
