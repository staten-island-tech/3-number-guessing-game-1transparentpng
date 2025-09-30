import random

guessHistory = []
guess = 0

genNumber = random.randint(0,100) # generates a random integer using the random library

while guess is not genNumber:
    guess = int(input("Try to guess the generated number!!")) # converts the input to integer
    if guess == genNumber:
        print(f"Congrats, You got it right! The generated number was {genNumber}.")
        print(f"Past Guesses: {guessHistory}")
    elif guess < genNumber:
        print("WRONG!!!!!!! Too low of a number!")
        print(f"Past Guesses: {guessHistory}")
        guessHistory.append(guess)
    elif guess > genNumber:
        print("WRONG!!!!!!! Too high of a number!")
        print(f"Past Guesses: {guessHistory}")
        guessHistory.append(guess)


        
        # / o o \
        # \  U  /
    