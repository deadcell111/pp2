"""Example
Change the second item:"""

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

"""Example
Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

"""Example
Change the second value by replacing it with two new values:"""

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

"""Example
Change the second and third value by replacing it with one value:"""

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

"""Example
Insert "watermelon" as the third item:"""

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)