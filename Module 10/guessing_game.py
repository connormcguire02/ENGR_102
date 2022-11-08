# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Connor McGuire
# Section:      563
# Assignment:   Lab 10.14
# Date:         3 11 2022

# creating a function that compares it to the number 26
def guesser(num):
    # counter must be global because even if bad input. it's still a guess
    # checking to see if the string has a decimal
    while not num.isdigit():
        num = input("Bad input! Try again: ")
        # counter += 1
    if num.isdigit():
        num = int(num)
    # a try except block to make sure  the program works properly
    if num > 26:
        return "Too high!"
    elif num < 26:
        return "Too low!"
    return 0

def main():
    print("Guess the secret number! Hint: it's an integer between 1 and 100...")
    guess = input("What is your guess? ")
    # counter is set to 1 because of the weird way my program works
    counter = 1
    compare = guesser(guess)
    while compare != 0:
        print(compare)
        guess = input("What is your guess? ")
        counter += 1
        compare = guesser(guess)
    try:
        print(f"You guessed it! It took you {counter} guesses.")
    except:
        print("",end="")
    
if __name__ == "__main__":
    main()