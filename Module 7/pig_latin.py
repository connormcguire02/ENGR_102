# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Connor McGuire
# Section:      563
# Assignment:   Lab 5.4
# Date:         4 10 2022

# defining a function that determines whether a string starts with a vowel
def aeiouy(string):
    if string[0] == "a" or string[0] == "e" or string[0] == "i" or string[0] == "o" or string[0] == "u" or string[0] == "y":
        return True
    else:
        return False

# prompting the user to enter words to be converted to pig latin
user_prompt = input("Enter word(s) to convert to Pig Latin: ")
# print(aeiouy(user_prompt))

# spliting the user prompt into a list seperated by spaces
word_list = user_prompt.rsplit(" ")
# print(word_list[2][2])

# creating a string that i add each word to after conversion
pig_latin = ""

# creating an iterator that goes through each word. i need this because java has a method that does this for you
charAt = 0

# creating a loop to traverse through the list of words and convert each word seperately
for i in word_list:
    if aeiouy(i[0]):
            i += "yay"
    else:
        for j in i:
            if aeiouy(i[0]) == False:
                i = i[1:] + i[0]
                # print(i)
        i += "ay"
    pig_latin += i + " "
print(f'In Pig Latin, "{user_prompt}" is: {pig_latin}')