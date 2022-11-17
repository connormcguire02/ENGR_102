# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Connor McGuire
# Section:      563
# Assignment:   Lab 9.16
# Date:         28 10 2022

# creating an object that will be used to write to the file
filewriter = open("coins.txt", "w")

with open("game.txt", "r") as filehandler:
    # creates a string that consists of the entire file
    entire_text = filehandler.read()
    # splitting on each new line
    instructions = entire_text.split("\n")
    i = 0
    coin_accum = 0
    counter = 0
    # using a while loop becuase we only care about it ending when it goes over the length of the file
    while 0 <= i < len(instructions):
        # splitting on each instruction individually since not all instructions will be used
        instructions[i] = instructions[i].split()
        # if the first word on each line is any of these then it has operations
        if instructions[i][0] == 'none':
            i += 1
            continue
        if instructions[i][0] == 'coin':
            if '+' in instructions[i][1]:
                coin_accum += int(instructions[i][1][1:])
                filewriter.write(instructions[i][1][1:]+"\n")
            else:
                coin_accum -= int(instructions[i][1][1:])
                filewriter.write(str((-1)*int(instructions[i][1][1:]))+"\n")
            i += 1
            continue
        if instructions[i][0] == 'jump':
            if '+' in instructions[i][1]:
                i += int(instructions[i][1][1:])
                filewriter.write(instructions[i][1][0]+"\n")
            else:
                i = i - int(instructions[i][1][1:])
            continue
    # print the total number of coins
    print(f"Total coins collected: {coin_accum}")
    

