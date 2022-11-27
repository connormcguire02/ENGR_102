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
    avg_wind_speed = []
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
        avg_wind_speed += [int(entire_text[i][1])]
        max_temp += [int(entire_text[i][4])]
        min_temp += [int(entire_text[i][5])]
        precipitation += [float(entire_text[i][2])]
    # print(data_2019)