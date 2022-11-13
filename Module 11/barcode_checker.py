# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Connor McGuire
# Section:      563
# Assignment:   Lab 11.11
# Date:         11 11 2022
filename = input("Enter the name of the file: ")

# barcodes is the name of the list of all the barcodes
barcodes = []

# filewriter is the object used to write the valid barcodes to the text file
filewriter = open("valid_barcodes.txt", "w")

with open(filename, "r") as filehandler:
    # splitting the file into each individual barcode
    entire_text = filehandler.read()
    barcodes = entire_text.split("\n")
    j = 0
    i = 0
    # going through each barcode and checking validity
    while i < len(barcodes):
        sum_first = 0
        sum_second = 0
        first_group = []
        second_group = []
        # going through each character
        while j < len(barcodes[i])-1:
            if j % 2 == 0:
                first_group += [int(barcodes[i][j])]
            else:
                second_group += [int(barcodes[i][j])]
            j += 1
        # performing validity calculations
        sum_first = sum(first_group)
        sum_second = sum(second_group)
        sum_second *= 3
        sum_first += sum_second
        sum_first %= 10
        sum_first = 10 - sum_first
        # removing the barcode if invalid or writing it if it is valid
        if sum_first != int(barcodes[i][-1]):
            barcodes.pop(i)
            i -= 1
        else:
            filewriter.writelines(barcodes[i]+"\n")
        i += 1
        j = 0
    print(f"There are {len(barcodes)} valid barcodes")

    