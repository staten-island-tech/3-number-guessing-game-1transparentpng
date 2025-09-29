import math

guessHistory = []
guess = 0

genNumber = 

while guess is not genNumber:
    guess = input("Try to guess the generated number!!")
    if guess < genNumber:
        print("WRONG!!!!!!! Too low of a number!")
        print(f"Past Guesses: {guessHistory}")
        guessHistory.append(guess)
    elif guess > genNumber:
        print("WRONG!!!!!!! Too high of a number!")
        print(f"Past Guesses: {guessHistory}")
        guessHistory.append(guess)