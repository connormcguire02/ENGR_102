# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ashley Brown
#               Connor McGuire
#               Gretta Weich
#               Collin Alexander
# Section:      563
# Assignment:   Lab 4.13: Make Change
# Date:         09/23/22

# gathering inputs for variables
payment = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))
change = payment - cost
change = round(change, 2)
# We will print how much change is left over based on the change variable, rounding it to 2 decimal places
print(f"You received ${change:.2f} in change. That is...")
# Now we determine numbers of dollars, quarters, dimes, nickels, and pennies based on their amounts,
# and print how much change the person will receive in coin integers
dollars = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0
if change >= 1:
    dollars = change // 1
    change %= 1
    change = round(change, 2)
    if dollars == 1:
        print(f"{int(dollars)} dollar")
    else:
        print(f"{int(dollars)} dollars")
if change >= 0.25:
    quarters = change // 0.25
    change %= 0.25
    change = round(change, 2)
    if quarters == 1:
        print(f"{int(quarters)} quarter")
    else:
        print(f"{int(quarters)} quarters")
if change >= 0.10:
    dimes = change // 0.10
    change %= 0.10
    change = round(change, 2)
    if dimes == 1:
        print(f"{int(dimes)} dime")
    else:
        print(f"{int(dimes)} dimes")
if change >= 0.05:
    nickels = change // 0.05
    change %= 0.05
    change = round(change, 2)
    if nickels == 1:
        print(f"{int(nickels)} nickel")
    else:
        print(f"{int(nickels)} nickels")
if change >= 0.01:
    pennies = change / 0.01
    if pennies == 1:
        print(f"{int(pennies)} penny")
    else:
        print(f"{int(pennies)} pennies")