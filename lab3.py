class Strings:
    def __init__(self):
        self.text = ""
    def getString(self):
        self.text = input()
    def printString(self):
        print(self.text.upper())
#Example:
if __name__ == "__main__":
    obj = Strings()
    obj.getString()
    obj.printString()