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
file_name = input('Enter the name of the file: ')
scanned_passports = open(file_name, 'r')
scanned_passports_list = scanned_passports.read().split('\n\n')
valid_passports_list = []
valid_passports_list_split = []
# Makes sure all the correct fields are in the passport
for passport in scanned_passports_list:
    if 'byr' in passport and 'iyr' in passport and 'eyr' in passport and 'hgt' in \
            passport and 'ecl' in passport and 'pid' in passport and 'cid' in passport:
        valid_passports_list.append(passport)
        valid_passports_list_split.append(passport)
# Splits the list o passports into their individual fields
for i in range(len(valid_passports_list_split)):
    valid_passports_list_split[i] = valid_passports_list_split[i].split('\n')
    valid_passports_list_split[i] = ' '.join(valid_passports_list_split[i]).split()
    for j in range(len(valid_passports_list_split[i])):
        valid_passports_list_split[i][j] = valid_passports_list_split[i][j].split(':')
num_valid_passports = 0
valid_passports2 = open('valid_passports2.txt', 'w')
valid_passports_list2 = []
# Makes sure every field is valid and that there are no repeats and if not then it is added to the file
for i in range(len(valid_passports_list_split)):
    req_fields_checked = 0
    for field in valid_passports_list_split[i]:
        if field[0] == 'byr':
            if 1920 <= int(field[1]) <= 2005:
                req_fields_checked += 1
            else:
                break
        elif field[0] == 'iyr':
            if 2012 <= int(field[1]) <= 2022:
                req_fields_checked += 1
            else:
                break
        elif field[0] == 'eyr':
            if 2022 <= int(field[1]) <= 2032:
                req_fields_checked += 1
            else:
                break
        elif field[0] == 'hgt':
            if 'cm' in field[1] and 150 <= int(field[1].strip('cm')) <= 193:
                req_fields_checked += 1
            elif 'in' in field[1] and 59 <= int(field[1].strip('in')) <= 76:
                req_fields_checked += 1
            else:
                break
        elif field[0] == 'ecl':
            if field[1] == 'amb' or field[1] == 'blu' or field[1] == 'brn' or field[1] == 'gry'\
                    or field[1] == 'grn' or field[1] == 'hzl' or field[1] == 'oth':
                req_fields_checked += 1
            else:
                break
        elif field[0] == 'pid':
            if len(field[1]) == 9:
                req_fields_checked += 1
            else:
                break
        elif field[0] == 'cid':
            if len(field[1].lstrip('0')) == 3:
                req_fields_checked += 1
            else:
                break
        if req_fields_checked == 7 and not(valid_passports_list[i] in valid_passports_list2):
            num_valid_passports += 1
            valid_passports_list2.append(valid_passports_list[i])
            valid_passports2.write(valid_passports_list[i] + '\n\n')
valid_passports2.close()
scanned_passports.close()
print(f'There are {num_valid_passports} valid passports')

    
