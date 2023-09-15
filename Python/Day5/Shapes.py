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
        return "Squares {} info".format(info)
    def sidesinfo(self,length):
        return "each side is {} cm".format(length)


class Rectangle(Shapes):

    def shapeinfo(self, info):
        return "Rectangles {} info".format(info)

    def sidesinfo(self,side1,side2):
        return "Rectangles {} side1 {} side2".format(side1).format(side2)


squarey = Square()      


print(squarey.shapeinfo("have 4 equal sides"))
print(squarey.sidesinfo("4 !"))

rectangley = Rectangle()

print(rectangley.shapeinfo("have 2 long equal sides and 2 short equal sides"))
print(squarey.sidesinfo("4 !","3"))