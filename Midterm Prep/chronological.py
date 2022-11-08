months = [
    "January","February","March",
    "April","May","June",
    "July","August","September",
    "October","November","December"
]

month_list = []
# take in 5 user input
for i in range(1,6):
    month_list += [input("User "+str(i)+" enter a birthday: ").split()]

dates = {month:[] for month in months}
#print(dates)
for entry in month_list:
    dates[entry[0]] += [int(entry[1])]
print(dates)
