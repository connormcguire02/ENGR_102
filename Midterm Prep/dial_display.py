dial = {
    2 : "ABC",
    3 : "DEF",
    4 : "GHI",
    5 : "JKL",
    6 : "MNO",
    7: "PQRS",
    8 : "TUV",
    9: "WXYZ"
}

dial_input = input("Enter a phone number XXX-XXXXXXXX: ")
dial_input_list = []

for i in dial_input:
    dial_input_list += [i]

for i in dial_input_list:
    for j in dial:
        if dial[j].__contains__(str(i)):
            i = j

print(dial_input_list)