accum = 0
with open("daythreeinput.py", 'r') as fileID:
    entire_text = fileID.read()
    entire_text = entire_text.split("\n")
    for i in range(len(entire_text)):
        first_half = entire_text[i][:]