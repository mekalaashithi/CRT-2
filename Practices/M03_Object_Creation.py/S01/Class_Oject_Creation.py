class Example:
    x = 100
    def display(slef):
        print("This is Example class display method")
obj = Example()
print(obj.x)
obj.display()

#Class Circle with 2 methods 
from math import pi
class Circle:
    r = 7
    def Area(self):
        return pi * self.r * self.r
    def preimeter(self):
        return 2 * pi * self.r
c = Circle()
print(c.Area())
print(c.Perimeter())
