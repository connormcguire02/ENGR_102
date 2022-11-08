clock = ["1","2",":","5","6"]

n = 0
while n < len(clock):
    if clock[n] == "1":
        clock[n] = one
    elif clock[n] == "2":
        clock[n] = two
    elif clock[n] == "3":
        clock[n] = three
    elif clock[n] == "4":
        clock[n] = four
    elif clock[n] == "5":
        clock[n] = five
    elif clock[n] == "6":
        clock[n] = six
    elif clock[n] == "7":
        clock[n] = seven
    elif clock[n] == "8":
        clock[n] = eight
    elif clock[n] == "9":
        clock[n] = nine
    elif clock[n] == "0":
        clock[n] = zero
    else:
        clock[n] = colon