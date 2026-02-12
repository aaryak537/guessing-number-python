import random
number=random.randint(1,100)
attempts=5
print("Guess the number game")
print("I have selected a number between 1 and 100.")
print("You have 5 attempts to guess it.\n")
while attempts>0:
    guess=int(input("Enter your guess:"))
    if guess==number:
        print("Correct! You guessed the number.")
        break
    elif guess<number:
        print("Too Low!")
    else:
        print("Too High")
    attempts-=1
    print("Attempts left:",attempts)
if attempts==0:
    print("\n Game Over! The correct number was ",number)