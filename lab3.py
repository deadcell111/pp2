import math

class Point:    
    def __init__(self, x = None, y = None):
        if x is None and y is None:
            x = int(input())
            y = int(input())
        self.x = x
        self.y = y

    def show(self):
        print(self.x, " ", self.y)
        
    def move(self, nx = None, ny = None):
        if nx is None and ny is None:
            nx = int(input())
            ny = int(input())
        
        self.x = nx
        self.y = ny
        
    def dist(self, d):
        print(math.sqrt((self.x - d.x) ** 2 + (self.y - d.y) ** 2))
#Example:
if __name__ == "__main__":
    p1 = Point()
    p2 = Point()
    print("First point is: ")
    p1.show()
    print("Second point is: ")
    p2.show()
    p1.move()
    print("First changed point: ")
    p1.show()
    print("The distant between 2 points: ")
    p1.dist(p2)
