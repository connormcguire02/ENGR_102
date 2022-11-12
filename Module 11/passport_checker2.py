filename = input("Enter the name of the file: ")

valid_ids = []

with open(filename, "r") as filehandler:
    entire_text = filehandler.read()
    passport_list = entire_text.split("\n\n")
    # print(len(passport_list))
    for info in passport_list:
        if 'byr' not in info or 'iyr' not in info or 'eyr' not in info or 'hgt' not in info or 'ecl' not in info or 'pid' not in info or 'cid' not in info:
            continue
        else:
            valid_ids.append(info)
    # print(len(valid_ids))

    # going through and splitting the data appropriately
    for i in range(len(valid_ids)):
        valid_ids[i] = valid_ids[i].split()
        for j in range(len(valid_ids[i])):
            valid_ids[i][j] = valid_ids[i][j].split(":")
    
    # going through the list of lists of lists and determining if each data is valid
    # since in my method, i am removing items from the list instead of adding them to another list, itterating through the loop will be different
    i = 0
    while i < len(valid_ids):
        for j in range(len(valid_ids[i])):
            if valid_ids[i][j][0] == 'byr' and 1920 <= int(valid_ids[i][j][1]) <= 2005 and len(valid_ids[i][j][1]) == 4:
                continue
            elif valid_ids[i][j][0] == 'iyr' and 2012 <= int(valid_ids[i][j][1]) <= 2022 and len(valid_ids[i][j][1]) == 4:
                continue
            elif valid_ids[i][j][0] == 'eyr' and 2022 <= int(valid_ids[i][j][1]) <= 2032 and len(valid_ids[i][j][1]) == 4:
                continue
            elif valid_ids[i][j][0] == 'hgt' and ("cm" in valid_ids[i][j][1] or "in" in valid_ids[i][j][1]):
                if "cm" in valid_ids[i][j][1]:
                    height = valid_ids[i][j][1].split('c')
                    if 150 <= int(height[0]) <= 193:
                        continue
                    else:
                        valid_ids.pop(i)
                        i -= 1
                        break
                if "in" in valid_ids[i][j][1]:
                    height = valid_ids[i][j][1].split('i')
                    if 59 <= int(height[0]) <= 76:
                        continue
                    else:
                        valid_ids.pop(i)
                        i -= 1
                        break
            elif valid_ids[i][j][0] == 'ecl' and (valid_ids[i][j][1]=='amb' or valid_ids[i][j][1]=='blu' or valid_ids[i][j][1]=='brn' or valid_ids[i][j][1]=='gry' or valid_ids[i][j][1]=='grn' or valid_ids[i][j][1]=='hzl' or valid_ids[i][j][1]=='oth'):
                continue
            elif valid_ids[i][j][0] == 'pid' and len(valid_ids[i][j][1]) == 9:
                continue
            elif valid_ids[i][j][0] == 'cid' and 1 <= (int(valid_ids[i][j][1]))/100 < 10:
                continue
            elif valid_ids[i][j][0] == 'hcl':
                continue
            else:
                valid_ids.pop(i)
                # this i -= 1 here is because the indecies all decriment by one whenever you pop a value out of the list
                i -= 1
                break
        i += 1
    print(f"There are {len(valid_ids)} valid passports")
    
