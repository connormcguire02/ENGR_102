# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Connor McGuire
# Section:      563
# Assignment:   Lab 5.4
# Date:         7 10 2022

def bubbleSort(a, bool):
    if isinstance(a, str):
        b = ""
        a_list = sorted(a, reverse=bool)
        n = 0
        while n < len(a_list):
            b += a_list[n]
            n += 1
        return b

#prompting the user to enter a 4 digit number
string_number = input("Enter a four-digit integer: ")
number = int(string_number)
n = 0
while n < 3:
    # the loop needs a reinitialization of the string number
    string_number = str(number)

    # initializing the reversed numbers
    string_sorted = ""
    number_backwards = 0

    # using my sort method to sort the string
    string_descending = bubbleSort(string_number, True)
    string_ascending = bubbleSort(string_number, False)
    number_ascending = int(string_ascending)
    number_descending = int(string_descending)
    # print("String ascending:",string_ascending)
    # print("String descending:",string_descending)

    # finding which number is bigger and subtracting the bigger from the smaller
    number = abs(number_ascending-number_descending)
    # print(number)
    n += 1