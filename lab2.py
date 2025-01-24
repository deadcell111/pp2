"""Example
Print the second item in the tuple:"""

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

"""Example
Print the last item of the tuple:"""

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

"""Example
Return the third, fourth, and fifth item:"""

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

"""Example
This example returns the items from the beginning to, but NOT included, "kiwi":"""

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

"""Example
This example returns the items from "cherry" and to the end:"""

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

"""Example
This example returns the items from index -4 (included) to index -1 (excluded)"""

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

"""Example
Check if "apple" is present in the tuple:"""

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")