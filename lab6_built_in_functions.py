"""Write a Python program with builtin function to multiply all the numbers in a list
Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
Write a Python program with builtin function that checks whether a passed string is palindrome or not.
Write a Python program that invoke square root function after specific milliseconds.
Sample Input:
25100
2123
Sample Output:
Square root of 25100 after 2123 miliseconds is 158.42979517754858
Write a Python program with builtin function that returns True if all elements of the tuple are true."""
import math
import time
list = [1,2,3,4,5]
string = "ChillGuy"
my_tuple = (True,True,True)
#Task 1: 
def product(a):
    return math.prod(a)
print(product(list))

#Task 2: 
def case(s):
    upper_case = sum(map(str.isupper, s))
    lower_case = sum(map(str.islower, s))
    print("Upper case: ", upper_case)
    print("Lower_case: ", lower_case)
case(string)

#Task 3:
def palindrome(s):
    r = reversed(s)
    return r == s
print(palindrome(string))

#Task 4:
def invoke_square():
    integer = int(input())
    ml_sec = int(input())
    time.sleep(ml_sec/1000)
    print(f"Square root of {integer} after {ml_sec} miliseconds is {math.sqrt(integer)}!")
invoke_square()

#Task 5: 
def check_tuple(t):
    return all(t)
print(check_tuple(my_tuple))