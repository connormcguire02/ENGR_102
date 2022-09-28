from random import randint

MaxGuesses = 5
print("See if you can guess the number I'm thinking of!")
secret_number = randint(1,10)
nGuesses = 0
while nGuesses < 100:
    print(secret_number)
    secret_number = randint(1,10)
    nGuesses += 1