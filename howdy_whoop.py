# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Connor McGuire
# Section:      563
# Assignment:   Lab 5.4
# Date:         29 9 2022

# prompting the user to enter two numbers
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

# creating a loop that will go through all 100 numbers and check for divisibility
i = 1
while i <= 100:
    if i%num1 == 0 and i%num2 == 0:
        # print(i)
        print("Howdy Whoop")
    elif i%num1 == 0:
        # print(i)
        print("Howdy")
    elif i%num2 == 0:
        # print(i)
        print("Whoop")
    else:
        print(i)
    i += 1