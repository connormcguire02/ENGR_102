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
     for i in instructions:
        i = i.split()
