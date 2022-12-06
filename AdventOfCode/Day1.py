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
        accum = 0
    
    accum = 0
    for _ in range(3):
        accum += max(total)
        for i in range(len(total)):
            if total[i] == max(total):
                total.pop(i)
                break
    print(accum)
    