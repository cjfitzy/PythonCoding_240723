# The Abstract Base Class
from abc import ABC, abstractmethod 

class Shapes(ABC):

    def __init__(self):
        pass
    
    @abstractmethod
    def shapeinfo(self):
        pass

    @abstractmethod
    def sidesinfo(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Square(Shapes):
    
    def shapeinfo(self,info):
        return "A {} is a four-sided shape with all sides equal in length".format(info)
    def sidesinfo(self,length):
        return "Each side is {} cm".format(length)
    def area(self,length):
        squarearea = int(length) * int(length)
        return "area = {} * {} which equals " + str(squarearea) + "cm".format(length)
        


class Rectangle(Shapes):

    def shapeinfo(self, info):
        return "A {}  is a four-sided shape with two sets of parallel sides".format(info)

    def sidesinfo(self,side1,side2):
        return "The two longer sides are {} cm and two shorter sides are {} cm".format(side1,side2)
    def area(self,side1,side2):
        recarea = int(side1) * int(side2)
        return "area = {}* {} which equals " + str(recarea) + "cm"

squarey = Square()      


print(squarey.shapeinfo("Square"))
print(squarey.sidesinfo("4"))
print(squarey.area("4"))
rectangley = Rectangle()

print(rectangley.shapeinfo("Rectangle"))
print(rectangley.sidesinfo("4","3"))
print(rectangley.area("4","3"))