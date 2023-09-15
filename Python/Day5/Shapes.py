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


class Square(Shapes):
    
    def shapeinfo(self,info):
        return "A {} is a four-sided shape with all sides equal in length".format(info)
    def sidesinfo(self,length):
        return "Each side is {} cm".format(length)


class Rectangle(Shapes):

    def shapeinfo(self, info):
        return "A {}  is a four-sided shape with two sets of parallel sides".format(info)

    def sidesinfo(self,side1,side2):
        return "The two longer sides are {} cm and two shorter sides are {} cm".format(side1,side2)


squarey = Square()      


print(squarey.shapeinfo("Square"))
print(squarey.sidesinfo("4"))

rectangley = Rectangle()

print(rectangley.shapeinfo("Rectangle"))
print(rectangley.sidesinfo("4","3"))