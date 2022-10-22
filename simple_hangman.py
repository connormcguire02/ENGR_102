user_1_input = input("Player one enter a secret word: ")
user_2_guess = input("Enter a guess: ")
while user_1_input.__contains__(user_2_guess):
    user_2_guess = input("Enter another guess: ")
print(f"Yay you guessed {user_1_input}")