# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ashley Brown
#               Connor McGuire
#               Gretta Weich
#               Collin Alexander
# Section:      563
# Assignment:   Lab 11.10
# Date:         11/10/22
foldername = r"c:\Users\conno\Python Projects\GitHub\ENGR_102\ENGR_102\Module 11"
filename = input("Enter the name of the file: ")

valid = 0

validpass = open(r'c:\Users\conno\Python Projects\GitHub\ENGR_102\ENGR_102\Module 11\valid_passports.txt', 'w') # create the valid passports file

valid_list = []

valid_ones = []

with open(filename, "r+") as filehandler: # open the file
    read = filehandler.read()  # make the file a long string
    passlist = read.split('\n\n')  # make the file list based on passport
    for passport in passlist:
        if 'byr' not in passport or 'iyr' not in passport or 'eyr' not in passport or 'hgt' not in passport or 'ecl' not in passport or 'pid' not in passport or 'cid' not in passport:  # if not valid, go to next passport
            continue
        else:  # if valid, add number to valid variable
            valid_ones.append(passport)
    valid_list = valid_ones[:]
    for i in range(len(valid_list)):
        valid_list[i] = valid_list[i].split('\n')
        valid_list[i] = ' '.join(valid_list[i])
        valid_list[i] = valid_list[i].split()
        for j in range(len(valid_list[i])):
            valid_list[i][j] = valid_list[i][j].split(':')
    for i in range(len(valid_list)):
        for j in range(len(valid_list[i])):
            yes = True
            if valid_list[i][j][0] == 'byr':
                if 1920 > int(valid_list[i][j][1]) or 2005 < int(valid_list[i][j][1]):
                    yes = False
                    break
            elif valid_list[i][j][0] == 'iyr':
                if 2011 >= int(valid_list[i][j][1]) or 2023 <= int(valid_list[i][j][1]):
                    yes = False
                    break
            elif valid_list[i][j][0] == 'eyr':
                if 2022 > int(valid_list[i][j][1]) or 2032 <= int(valid_list[i][j][1]):
                    yes = False
                    break
            elif valid_list[i][j][0] == 'hgt':
                if 'cm' in valid_list[i][j][1]:
                    centi = valid_list[i][j][1].split('c')
                    if 150 >= int(centi[0]) or 193 <= int(centi[0]):
                        # print(centi)
                        yes = False
                        break # for some reason the code is still adding 66 cm passport to the valid_passports2 file !!! i think height is the problem one, just kidding. it is also not catching other things and i dont get why
                    break
                elif 'in' in valid_list[i][j][1]:
                    inch = valid_list[i][j][1].split('i')
                    if 59 >= int(inch[0]) or 76 <= int(inch[0]):
                        yes = False
                        break
                    break
            elif valid_list[i][j][0] == 'ecl':
                if valid_list[i][j][1] != 'amb' and valid_list[i][j][1] != 'brn' and valid_list[i][j][1] != 'blu' and valid_list[i][j][1] != 'gry' and valid_list[i][j][1] != 'grn' and valid_list[i][j][1] != 'hzl' and valid_list[i][j][1] != 'oth':
                    yes = False
                    break
            elif valid_list[i][j][0] == 'pid':
                if len(valid_list[i][j][1]) != 9:
                    yes = False
                    break
            elif valid_list[i][j][0] == 'cid':
                num = int(valid_list[i][j][1])
                if len(str(num)) != 3:
                    yes = False
                    break
            if j == (len(valid_list[i][j]) - 1) and yes == True:
                validpass.write(valid_ones[i] + '\n\n')
                valid += 1

#print(valid_ones)
#print(valid_list)

print(f'There are {valid} valid passports')  # print the number of valid passports

validpass.close()  # close the valid passport file
