accum = 0
total = []
with open("dayoneinput.txt", "r") as fileID:
    entire_text = fileID.read()
    entire_text = entire_text.split("\n\n")
    for i in range(len(entire_text)):
        entire_text[i] = entire_text[i].split("\n")
        for j in range(len(entire_text[i])):
            accum += int(entire_text[i][j])
        total += [accum]
    print(max(total))
    