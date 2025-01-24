"""Example
Print the second item of the list:"""

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

"""Example
Print the last item of the list:"""

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

"""Example
Return the third, fourth, and fifth item:"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

"""Example
This example returns the items from the beginning to, but NOT including, "kiwi":"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

"""Example
This example returns the items from "cherry" to the end:"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

"""Example
This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

"""Example
Check if "apple" is present in the list:"""

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")