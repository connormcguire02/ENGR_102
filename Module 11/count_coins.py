# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Connor McGuire
# Section:      563
# Assignment:   Lab 9.16
# Date:         28 10 2022

with open("game.txt", "r") as filehandler:
     entire_text = filehandler.read()
     instructions = entire_text.split("\n")
     i = 0
     coin_accum = 0
     while i < len(instructions):
        instructions[i] = instructions[i].split()
        if instructions[i][0] == 'jump':
            if '+' in instructions[i][1]:
                i += int(instructions[i][1][1:])
            else:
                i -= int(instructions[i][1][1:])
        if instructions[i][0] == 'none':
            i += 1
        if instructions[i][0] == 'coin':
            if '+' in instructions[i][1]:
                coin_accum += int(instructions[i][1][1:])
            else:
                coin_accum -= int(instructions[i][1][1:])

