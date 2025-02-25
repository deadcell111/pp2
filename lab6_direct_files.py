import os
import string
"""
Write a Python program to list only directories, files and all directories, files in a specified path.
Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
Write a Python program to count the number of lines in a text file.
Write a Python program to write a list to a file.
Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
Write a Python program to copy the contents of a file to another file
Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
"""
 #Attention!!! If you wanna create 26 files in Task 6 and see the your directory at the Task 1, delete a '#' before the function. 

#1 Task: 
def content(path):
    all_items = os.listdir(path)
    directories = [i for i in all_items if os.path.isdir(os.path.join(path, i))]
    files = [i for i in all_items if os.path.isfile(os.path.join(path,i))]
    all = [i for i in all_items]
    print(f"All directories in {path}",directories)
    print(f"Only files in {path}", files)
    print(f"All in {path}", all)
path = os.path.expanduser("~")
#content(path)

#Task 2: 
if os.path.exists(path):
    print(f"Yes, path {path} exists")
else:
    print(f"No,path {path} doesnt exists")

if os.access(path, os.W_OK):
    print(f"The path {path} are writable")
else:
    print(f"No,path {path} are not writable")

if os.access(path, os.X_OK):
    print(f"The path {path} are excecutable")
else:
    print(f"No,path {path} are not executable")

#Task 3: 
def test_path(path):
    if os.path.exists(path):
        print(f"Yes, path {path} exists, filname: {os.path.basename}, dirname: {os.path.dirname}")
    else:
        print(f"No,path {path} doesnt exists")
test_path(path)

#Task 4: 
f = open("demofile.txt","r+")
w = open("writable_file","w")
print(f.read())
with open("demofile.txt") as f:
    print(len(f.readlines()))

#Task 5: 
list = ["P.Diddy ","is ","pdf ","file"]
with open("writable_file.txt","w") as w:
    w.writelines(list)

#Task 6: 
def generator():
    for letter in string.ascii_uppercase:
        with open(letter + ".txt","w") as g:
            g.write(letter)
#generator()

#Task 7:
with open("demofile.txt",'r') as first, open('copy.txt','w') as second:
    for line in first:
        second.write(line)

#Task 8"
ur_path = input("Enter your path name: ")
def remove_file(ur_path):
    if os.path.exists(ur_path):
        if os.access(path, os.W_OK):
            os.remove(ur_path)
            print("File is removed succesfully")
        else:
            print("This file is not accesible")
    else:
        print(f"No, path {ur_path} doesnt exists")

remove_file(ur_path)