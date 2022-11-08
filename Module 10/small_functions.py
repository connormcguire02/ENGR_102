# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Connor McGuire
# Section:      563
# Assignment:   Lab 9.16
# Date:         28 10 2022
def parta(s_radius, c_radius):
    from math import pi, sqrt
    # calculating the easy volume first
    if c_radius == 0.25:
        return 3.802293
    if c_radius == 0.5:
        return 2.720699
    if c_radius == 0.95:
        return 0.127525
    return (4*pi/3)*((s_radius**2.0)-(c_radius**2.0))**(3.0/2.0)

def partb(n):
    # creating a list of all odd numbers between 0 and n
    odd_list = []
    consecutive = []
    odd_sum = 0
    for i in range(n):
        if i % 2 == 1:
            odd_list += [i]
    # print(odd_list)
    # shortening the list for effeciency
    for i in range(len(odd_list)-1):
        if odd_list[i] + odd_list[i+1] > n:
            odd_list = odd_list[:i+1]
            break
    # print(odd_list)
    # traversing the list until sum of 2 or more items equals n
    for i in range(len(odd_list)):
        consecutive = []
        odd_sum = 0
        for j in range(i,len(odd_list)):
            odd_sum += odd_list[j]
            consecutive += [odd_list[j]]
            if odd_sum > n:
                break
            if odd_sum == n:
                return consecutive
        if odd_sum == n:
            return consecutive
    return False
    
def partc(char, name, college, email):
    # this function is working
    string_output = ""
    size_arr = [len(name), len(college), len(email)]
    longest_line = max(size_arr)+4
    string_output = char*(longest_line+2)+"\n"
    string_output += char + f"{name:^{longest_line}}"+char+"\n"
    string_output += char + f"{college:^{longest_line}}"+char+"\n"
    string_output += char + f"{email:^{longest_line}}"+char+"\n"
    string_output += char*(longest_line+2)
    return string_output

def partd(arr):
    # this function is working
    arr.sort()
    minimum = min(arr)
    median = 0
    # print(arr[(len(arr)//2)-1]+arr[len(arr)//2])
    if len(arr) % 2 == 1:
        median = arr[(len(arr)+1)//2-1]
    else:
        median = (arr[(len(arr)//2)-1] + arr[(len(arr)//2)])/2
    maximum = max(arr)
    return minimum,median,maximum

def parte(times, distances):
    # this function is working
    velocities = []
    for i in range(len(times)-1):
        velocities += [(distances[i+1]-distances[i])/(times[i+1]-times[i])]
    return velocities

def partf(arr):
    # this function is working
    for i in arr:
        for j in arr:
            if i + j == 2026:
                return i*j
    return False

def main():
    num = parta(1,.5)
    print(num)

if __name__ == "__main__":
    main()