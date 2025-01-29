def Centigrade(F):
    C = (5/9) * (F - 32)
    return C
F = int(input("Farenheit: "))
print("In Centigrade: ",Centigrade(F))   