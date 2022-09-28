# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ashley Brown
#               Connor McGuire
#               Gretta Weich
#               Collin Alexander
# Section:      563
# Assignment:   Lab 5: Diabetes Risk
# Date:         09/23/22
# Gathering inputs and converting the inputs to the amount of risk it adds
# Gender
sex = input("Enter your sex (M/F): ").upper()
if sex == 'F':
    sex = .879 # The weighted value for sex
else:
    sex = 0
# age
age = float(input("Enter your age(years):"))
# bmi
BMI = float(input("Enter your BMI:"))
if BMI < 25:
    BMI = 0
elif BMI <= 27.49:
    BMI = 0.699 # the weighted bmi value for the age bounds
elif BMI <= 29.99:
    BMI = 1.97 # the weighted bmi value for the age bounds
else:
    BMI = 2.518 # the weighted bmi value for above 30 years old
# hypertension medication
hypertension = input("Are you on medication for hypertension (Y/N)?").upper()
if hypertension == 'Y':
    hypertension = 1.222 # the weighted value medications
else:
    hypertension = 0
# steroids C
steroids = input("Are you on steroids (Y/N)?").upper()
if steroids == 'Y':
    steroids = 2.191 # weighted value for steroids
else:
    steroids = 0
# smoker
smoker = input("Do you smoke cigarettes (Y/N)?").upper()
if smoker == 'Y':
    smoker = 0.855 # weighted value for current smoker
else:
    smoker = input("Did you used to smoke (Y/N)?").upper()
    if smoker == 'Y':
        smoker = -0.218 # weighted value for previous smoker
    else:
        smoker = 0
# family history
family_history = input("Do you have a family history of diabetes (Y/N)?").upper()
if family_history == 'N':
    family_history = 0
elif family_history == 'Y':
    family_history = input("Both parent and sibling (Y/N)?").upper()
    if family_history == 'Y':
        family_history = 0.753 # weighted value for both family members
    else:
        family_history = 0.728 # weighted value for one family member
# Calculating based on given equation
n =  6.322 + sex - (0.063 * age) - BMI - hypertension - steroids - smoker - family_history
# n is the total weight of the risk
from math import e
risk = 100 / (1 + (e**n)) # the risk calculation
print(f'Your risk of developing type-2 diabetes is {risk:.1f}%')

