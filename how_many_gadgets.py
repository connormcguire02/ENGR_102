days = int(input("Please enter a positive value for day: "))
number_of_gadgets = 0
if days <= 10:
    number_of_gadgets *= 5
if 10 < days < 60:
    number_of_gadgets = 50 + number_of_gadgets*50
# now the next part is a tad bit complicated for some reason
if 60 < days < 100:
    number_of_gadgets = 2550
    # gathering trapezoid info
    base_1 = 49
    height = days - 60
    base_2 = 110 - days
    area = (1/2)*(base_2+base_1)*height
    area = int(area)
    number_of_gadgets += area
if days > 100:
    number_of_gadgets = 2550
    area_trap = int((1/2)*(49+10)*40)
    number_of_gadgets += area_trap
if days < 0:
    print("You entered an invalid number!")
print(f"The total number of gadgets produced on day {days} is {number_of_gadgets}")
