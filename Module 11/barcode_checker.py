filename = input("Enter the name of the file: ")

first_group = []
second_group = []
barcodes = []

with open(filename, "r") as filehandler:
    entire_text = filehandler.read()
    barcodes = entire_text.split("\n")
    j = 0
    for i in barcodes:
        while j < len(i):
            if j % 2 == 0:
                first_group += [i[j]]
            else:
                second_group += [i[j]]
    