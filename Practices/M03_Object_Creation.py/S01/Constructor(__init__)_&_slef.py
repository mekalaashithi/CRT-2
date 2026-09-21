class A:
    count = 0
    def __init__(self):
        A.count += 1
a = A()
b = A()
c = A()
print("Object count is:" ,A.count)


from math import pi
class Circle:
    def __init__(self, r):
        self.r = r
    def Area(self):
        return pi * self.r * self.r
    def Perimeter(self):
        return 2 * pi * self.r
c = Circle(7)
c1 = Circle(10)
c2 = Circle(15)
print(c.Area())
print(c.Perimeter())
print(c1.Area())
print(c1.Perimeter())
print(c2.Area())
print(c2.Perimeter())



a= 10
b = 15.5
c = "Ram"
d = [ 1,2,3,4,5,6]
e = (1,2,3,4,5,6)
f = {1,2,3,4,5,6}
g = {"name":"Kalyani"}
print