# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Connor McGuire
# Section:      563
# Assignment:   Lab 5.4
# Date:         6 10 2022

# prompting the user to enter some text
user_prompt = input("Enter some text: ")
user_prompt = user_prompt.lower()
#spliting the string into a list on spaces
# word_list = user_prompt.rsplit(" ")
i_replace = ""
# creating loops that go through each word and each letter of each word
for i in user_prompt:
    if i == "a":
        i = "4"
    if i == "e":
        i = "3"
    if i == "o":
        i = "0"
    if i == "s":
        i = "5"
    if i == "t":
        i = "7"
    i_replace += i
# print(i_replace)
print(f'In leet speak, "{user_prompt}" is: {i_replace}')