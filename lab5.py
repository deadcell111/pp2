import re


"""Dear Menglibay, 
I hope I didn't make the wrong choice this time, and everything suits you, 
to make the program work, remove the '#' before 'print'."""


txt = """Dreams breathe life into men, and can cage them in suff_ering. 
Men life and die by their dreams, but long after they've been abbandoned, they still smolder deep in men's hearts. 
Some see nothing more than life and death. They are dead."""
lst = "under_score"
l = "akakfdakb"
text = "snake_case"
#Task 1, Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

x = r'a*b*'
str1_match = re.findall(x,txt)
#if str1_match:
    #print(str1_match)

#Task 2, Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

y = r'ab{2,3}'
str2_match = re.findall(y,txt)
#if str2_match:
    #print(str2_match)

#Task 3, Write a Python program to find sequences of lowercase letters joined with a underscore.

z = '^[a-z]+_[a-z]+$'
str3_match = re.findall(z,lst)
#if str3_match:
    #print("Yes")

#Task 4, Write a Python program to find the sequences of one upper case letter followed by lower case letters.

a = r'[A-Z][a-z]+'
str4_match = re.findall(a,txt)
#if str4_match:
    #print(str4_match)

#Task 5, Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

b = r'a*b$'
str5_match = re.findall(b,l)
#if str5_match:
    #print("Yes")

#Task 6, Write a Python program to replace all occurrences of space, comma, or dot with a colon.
str6_match = re.sub("[,.]",":",txt)
#print(str6_match)

#Task 7, Write a python program to convert snake case string to camel case string.
res = text.split('_')
camel = res[0] + ''.join(word.capitalize() for word in res[1:])
#print(camel)

#Task 8, Write a Python program to split a string at uppercase letters.
t = "MathIsGood"
str8_match = re.findall(r'[A-Z][^A-Z]*',t)
str8_match = ' '.join(str8_match)
#print(str8_match)

#Task 9, Write a Python program to insert spaces between words starting with capital letters.
def cap_between(text):
    res1 = re.findall(r'[A-Z][^A-Z]*',text)
    res1 = ' '.join(res1)
    return res1
r = "OmaeWaMou"
#print(cap_between(r))

#Task 10, Write a Python program to convert a given camel case string to snake case. 
s = "camelCaseYo"
snk = ""
for i in s:
    if i.isupper():
        snk += "_" + i.lower()
    else:
        snk += i.lower()
#print(snk)
