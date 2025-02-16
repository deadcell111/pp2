import math
#1
a = int(input("Input degree: "))
print(f"Output radian:",math.radians(a))
#2
h = int(input("Height: "))
f = int(input("Base, first value: "))
s = int(input("Base, second value: "))
area = ((f + s)/2) * h
print("Expected Output: ", area)
#3
side = int(input('Input number of sides: '))
length1 = int(input("Input the length of a side: "))
area2 = (side * length1 ** 2)/(4 * math.tan(math.pi / side))

print(f"Area of polygon: {area2}")
#4
lb = int(input("Length of base: "))
hb = int(input("Height of parallelogram: "))
print("Expected Output: ",lb * hb)