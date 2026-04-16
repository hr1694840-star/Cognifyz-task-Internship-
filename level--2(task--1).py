
import random

secret = random.randint(1, 100)

guess = 0

print("Guess a number between 1 and 100")

while guess != secret:
    guess = int(input("Enter your guess: "))
    
    if guess > secret:
        print("Too high!")
    
    elif guess < secret:
        print("Too low!")
    
    else:
        print("Correct! You guessed it 🎉")