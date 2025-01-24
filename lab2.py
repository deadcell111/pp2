"""Example
Remove "banana":"""

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

"""Example
Remove the first occurrence of "banana":"""

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

"""Example
Remove the second item:"""

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

"""Example
Remove the last item:"""

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

"""Example
Remove the first item:"""

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

"""Example
Delete the entire list:"""

thislist = ["apple", "banana", "cherry"]
del thislist

"""Example
Clear the list content:"""

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)