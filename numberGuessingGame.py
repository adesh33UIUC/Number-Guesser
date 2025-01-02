import random

print("\"Number Guessing Game\" - By Anish Deshpande")
guessed = False
randNum = random.randint(1, 10)
while guessed == False:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess > randNum:
        print('Your guess is higher than the value')
        
    elif guess < randNum:
        print('Your guess is lower than the value')
    else:
        print('You guessed the value correctly!!!')
        print('Value = ' + str(guess))
        guessed = True
