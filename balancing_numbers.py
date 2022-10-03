# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Connor McGuire
# Section:      563
# Assignment:   Lab 6.15
# Date:         29 9 2022

# Prompting the user to enter a number to be tested
balancing_number = int(input("Enter a value for n: "))
n = balancing_number - 1
temp = n

sum_before = 0
sum_after = 0
r = 1
# finding the sum of the numbers before n
while n > 0:
    sum_before += n
    # print(balancing_number)
    # print(sum_before)
    n -= 1
n = temp + 1
# print(n)
# print(r)

# now we have the sum on one side so now lets do a while loop to determine a possible value for r
while sum_after < sum_before:
    sum_after += n+r
    r += 1
if sum_after > sum_before:
    print(f"{balancing_number} is not a balancing number")
else:
    print(f"{balancing_number} is a balancing number with r={r-1}")

# print(sum_before)
# print(sum_after)
