import string
def is_palindrome(s):
    whilelist = set(string.ascii_lowercase)
    s = s.lower()
    s = ''.join([c for c in s if c in whilelist])
    return s == s[::-1]
s = input()
print(is_palindrome(s))