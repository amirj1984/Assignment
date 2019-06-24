# this program asks the user to guess a number and provides hints

from random import randint

secret_num = randint(1, 1000)

while True:
    num = int(input("guess a positive integer number from 1 to 1000 : "))
    if num > secret_num:
        print("your guessed number is GREATER than the secret number")
    elif num < secret_num:
        print("your guessed number is LESSER than the secret number")
    else:
        print("BINGO!")
        break
