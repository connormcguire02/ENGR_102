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

'''
• byr – Birth year – four digits, between 1920 and 2005, inclusive
• iyr – Issue year – four digits, between 2012 and 2022, inclusive
• eyr – Expiration year – four digits, between 2022 and 2032, inclusive
• hgt – Height – a number followed by either cm or in
o If cm, the number must be between 150 and 193, inclusive
o If in, the number must be between 59 and 76, inclusive
• hcl – Hair color – not required
• ecl – Eye color – exactly one of the following: amb, blu, brn, gry, grn, hzl, oth
• pid – Passport ID – a nine-digit number, including leading zeroes
• cid – Country ID – a three-digit number, NOT including leading zeroes

writes the valid passport scans to a new file named valid_passports2.txt.
'''

filename = input("Enter the name of the file: ")

valid = 0

validpass = open('valid_passports2.txt', 'w') # create the valid passports file

valid_list = []

# think we could use same baseline as first code
# and just add all the other checking things to it

with open(filename, "r+") as filehandler:
    read = filehandler.read()
    passlist = read.split('\n\n')
    for passport in passlist:
        personal_info = passport.split("\n")
    print(personal_info)
    valid_list = valid_list.split(" ", '\n') 
print(f'There are {valid} valid passports')

validpass.close()