# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Connor McGuire
# Section:      563
# Assignment:   Lab 11.13
# Date:         11 11 2022

# importing the mean function from stat to calculate averages
from statistics import mean

with open("WeatherDataCLL.csv", "r") as filehandler:
    # reading in the first line without saving it because i don't care
    filehandler.readline()
    # reading the entire file and then splitting on
    entire_text = filehandler.read()
    entire_text = entire_text.split("\n")
    data_2019 = []
    data_2020 = []
    data_2021 = []
    max_temp = []
    min_temp = []
    precipitation = []

    # going through the list of data and adding it to the appropriate lists
    for i in range(len(entire_text)-1):
        entire_text[i] = entire_text[i].split(",")
        if '2019' in entire_text[i][0]:
            data_2019 += [entire_text[i]]
        if '2020' in entire_text[i][0]:
            data_2020 += [entire_text[i]]
        if '2021' in entire_text[i][0]:
            data_2021 += [entire_text[i]]
        max_temp += [int(entire_text[i][4])]
        min_temp += [int(entire_text[i][5])]
        precipitation += [float(entire_text[i][2])]
    # print(data_2019)

print(f"3-year maximum temperature: {max(max_temp)} F")
print(f"3-year minimum temperature: {min(min_temp)} F")
print(f"3-year average precipitation: {mean(precipitation):.3f} inches")
print()

# prompting the user to enter a month and a year to retrieve the data for
temp = input("Please enter a month: ")
input_month = temp.lower()
input_year = input("Please enter a year: ")
print()

months =   [["january", '1'], ["february", '2'], ["march", '3'],
            ['april', '4'], ['may', '5'], ['june', '6'], ['july', '7'],
            ['august', '8'], ['september', '9'], ['october', '10'],
            ['november', '11'], ['december', '12']]
print(f"For {temp} {input_year}:")

# swapping the month name for the month number
for i in months:
    if input_month == i[0]:
        input_month = i[1]
        break

# generalizing each year as data
data = []
if input_year == '2019':
    data = data_2019
if input_year == '2020':
    data = data_2020
if input_year == '2021':
    data = data_2021

# making data only for the month prompted
i = 0
temp_data = []
wind_data = []
pre_percent = 0.0
while i < len(data):
    if len(input_month) == 1:
        if input_month != data[i][0][0:1]:
            data.pop(i)
            i -= 1
    if len(input_month) == 2:
        if input_month != data[i][0][0:2]:
            data.pop(i)
            i -= 1
    else:
        wind_data += [float(data[i][1])]
        if float(data[i][2]) > 0:
            pre_percent += 1
        temp_data += [int(data[i][4])]
    i += 1
# print(data)
print(f"Mean maximum daily temperature: {mean(temp_data):.1f} F")
print(f"Mean daily wind speed: {mean(wind_data):.2f} mph")
print(f"Percentage of days with precipitation: {pre_percent/len(data)*100:.1f}%")