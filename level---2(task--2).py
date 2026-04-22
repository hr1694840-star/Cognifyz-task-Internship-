import random

# set range
low = 1
high = 100

# generate random number
secret_number = random.randint(low, high)

print(f"Guess the number between {low} and {high}")

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Correct! You guessed the number.")
        break