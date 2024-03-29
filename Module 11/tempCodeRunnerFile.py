with open(foldername+"\\"+filename, "r+") as filehandler: # open the file
    read = filehandler.read() # make the file a long string
    passlist = read.split('\n\n') # make the file list based on passport
    for passport in passlist:
        if 'byr' not in passport or 'iyr' not in passport or 'eyr' not in passport or 'hgt' not in passport or 'ecl' not in passport or 'pid' not in passport or 'cid' not in passport: # if not valid, go to next passport
            continue
        else: # if valid, add number to valid variable
            valid_ones.append(passport)
            valid += 1
    valid_list = valid_ones
    for i in range(len(valid_list)):
        valid_list[i] = valid_list[i].split('\n')
        valid_list[i] = ' '.join(valid_list[i])
        valid_list[i] = valid_list[i].split()
        for j in range(len(valid_list[i])):
            valid_list[i][j] = valid_list[i][j].split(':')
    for i in range(len(valid_list)):
        for j in range(len(valid_list[i])):
            if valid_list[i][j][0] == 'byr':
                if 1920 <= int(valid_list[i][j][1]) <= 2005:
                    continue
                else:
                    break
            elif valid_list[i][j][0] == 'iyr':
                if 2011 < int(valid_list[i][j][1]) < 2023:
                    continue
                else:
                    break
            elif valid_list[i][j][0] == 'eyr':
                if 2022 <= int(valid_list[i][j][1]) <= 2032:
                    continue
            elif valid_list[i][j][0] == 'hgt':
                if 'cm' in valid_list[i][j][1]:
                    if 150 <= int(valid_list[i][j][1][0:3]) <= 193:
                        continue
                    else:
                        break
                elif 'in' in valid_list[i][j][1]:
                    if 59 <= int(valid_list[i][j][1][0:2]) <= 76:
                        continue
                    else:
                        break
                else:
                    break
            elif valid_list[i][j][0] == 'ecl':
                if valid_list[i][j][1] == 'amb' or valid_list[i][j][1] == 'brn' or valid_list[i][j][1] == 'blu' or valid_list[i][j][1] == 'gry' or valid_list[i][j][1] == 'grn' or valid_list[i][j][1] == 'hzl' or valid_list[i][j][1] == 'oth':
                    continue
                else: 
                    break
            elif valid_list[i][j][0] == 'pid':
                if len(valid_list[i][j][1]) == 9:
                    continue
                else:
                    break
            elif valid_list[i][j][0] == 'cid':
                if len(int(valid_list[i][j][1])) == 3:
                    continue
                else:
                    break
            else:
                continue
        # if valid_list[i][j] == valid_ones[j]:
            # validpass.write(valid_ones[j]='\n')
        
print(f'There are {valid} valid passports') # print the number of valid passports

validpass.close() # close the valid passport file