"""ExampleGet your own Python Server
Using the append() method to append an item:"""

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

"""Example
Insert an item as the second position:"""

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

"""Example
Add the elements of tropical to thislist:"""

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

"""Example
Add elements of a tuple to a list:"""

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)