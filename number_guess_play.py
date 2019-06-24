# this program reads a number from the user and if the guessed number is equal to the secret number, it is done
from random import randint

secret = randint(1, 10)
while True:
    num = int(input("guess an integer number from 1 to 10:"))
    if secret > num:
        print("your guess is LESS than the secret number")
    elif secret < num:
        print("your guess is GREATER than the secret number")
    else:
        print("you WON in guessing the secret number")
        break



