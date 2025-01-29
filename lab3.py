class Shape:
    def area(self):
        print(0)
class Rectangle(Shape):
    def __init__(self,length = None,width = None):
        if length is None and width is None:
            length = int(input())
            width = int(input())
        self.length = length
        self.width = width
    def area(self):
        print(self.length * self.width)
#Example:   
if __name__ == "__main__":
    obj = Shape()
    obj.area()
    rec = Rectangle()
    rec.area()