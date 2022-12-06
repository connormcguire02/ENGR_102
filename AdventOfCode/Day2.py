accum = 0
with open("daytwoinput.txt", 'r') as fileID:
    entire_text = fileID.read()
    entire_text = entire_text.split('\n')
    for i in range(len(entire_text)):
        entire_text[i] = entire_text[i].split()
        if entire_text[i][1] == 'X':
            if entire_text[i][0] == 'A':
                accum += 3
            if entire_text[i][0] == 'C':
                accum +=  2
            if entire_text[i][0] == 'B':
                accum += 1
            continue
        if entire_text[i][1] == 'Y':
            accum += 3
            if entire_text[i][0] == 'B':
                accum += 2
            if entire_text[i][0] == 'A':
                accum +=  1
            if entire_text[i][0] == 'C':
                accum += 3
            continue
        if entire_text[i][1] == 'Z':
            accum += 6
            if entire_text[i][0] == 'C':
                accum += 1
            if entire_text[i][0] == 'B':
                accum +=  3
            if entire_text[i][0] == 'A':
                accum += 2
            continue
    print(accum)