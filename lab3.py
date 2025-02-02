import random
print("Hello! What is your name?")
name = input()
print(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.")
x = random.randint(1,20)
rep = 0
t = True
while t:
        y = int(input())
        rep += 1
        if x != y:
            print("Your guess is too low.\nTake a guess.")
            t = True
        else:
            print(f"Good job, {name}! You guessed my number in {rep} guesses!")
            t = False

