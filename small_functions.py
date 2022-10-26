def parta(s_radius, c_radius):
    from math import pi, asin, cos, sqrt
    # calculating the easy volume first
    volume_sphere = (4/3)*pi*(s_radius**3)
    # It'll be easier to compute the volume of the dome in polar becuase we have r and enough to determine theta
    theta = asin(c_radius/s_radius)
    volume_dome = (pi/3)*(s_radius**3)*(2+cos(theta))((1-cos(theta))**2)
    # cylinder gets a little tricky with the height
    # the height of the cylinder can be found using some trig
    c_height = 2*sqrt((s_radius**2)-(c_radius**2))
    volume_cyninder = pi*(c_radius**2)*c_height
    return volume_sphere-volume_dome-volume_cyninder

def partb(n):
    # creating a list of all odd numbers between 0 and n
    odd_list = []
    consecutive = []
    odd_sum = 0
    for i in range(n):
        if i % 2 == 1:
            odd_list += [i]
    # shortening the list for effeciency
    for i in range(len(odd_list)-1):
        if odd_list[i] + odd_list[i+1]:
            odd_list = odd_list[:i]
    # traversing the list until sum of 2 or more items equals n
    for i in odd_list:
        consecutive = []
        odd_sum = 0
        while odd_sum < n:
            odd_sum += i
            consecutive += [i]
        if odd_sum == n:
            return consecutive
    return False
    
def partc(char, name, college, email):
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
    minimum = min(arr)
    median = arr[len(arr)//2]
    maximum = max(arr)
    return minimum,median,maximum

def parte(times, distances):
    velocities = []
    for i in range(times-1):
        velocities += [(distances[i+1]-distances[i])/(times[i+1]-times[i])]
    return velocities

def partf(arr):
    for i in arr:
        for j in arr:
            if i + j == 2026:
                return i*j
    return False

def main():
    pass

if __name__ == "__main__":
    main()