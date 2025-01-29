class Shape:
    def area(self):
        print(0)
class Square(Shape):
    def __init__(self,length):
        length = int(input())
        self.length = length
    def area(self):
        print(pow(self.length,2))
#Example:   
if __name__ == "__main__":
    obj = Shape()
    obj.area()
    square = Square(5)
    square.area()