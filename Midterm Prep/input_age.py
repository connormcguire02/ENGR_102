user_input = input("Please enter an age: ")
stored_ages = []
stored_ages += [int(user_input)]

while int(user_input) >= 0:
    user_input = input("Please enter an age: ")
    if int(user_input) >= 0:
        stored_ages += [int(user_input)]
    else:
        break

# printing max
print("Max: ", max(stored_ages))

#printing mix
print("Min: ", min(stored_ages))