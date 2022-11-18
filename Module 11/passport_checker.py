# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ashley Brown
#               Connor McGuire
#               Gretta Weich
#               Collin Alexander
# Section:      563
# Assignment:   Lab 11.9
# Date:         11/10/22

filename = input("Enter the name of the file: ")

valid = 0

validpass = open('valid_passports.txt', 'w') # create the valid passports file

with open(filename, "r+") as filehandler: # open the file
    read = filehandler.read() # make the file a long string
    passlist = read.split('\n\n') # make the file list based on passport
    for passport in passlist:
        if 'byr' not in passport or 'iyr' not in passport or 'eyr' not in passport or 'hgt' not in passport or 'ecl' not in passport or 'pid' not in passport or 'cid' not in passport: # if not valid, go to next passport
            continue
        else: # if valid, add number to valid variable
            valid += 1
            validpass.write(passport+'\n\n') # write into the valid passports file

print(f'There are {valid} valid passports') # print the number of valid passports

validpass.close() # close the valid passport file