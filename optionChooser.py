options = [
    "1. Learn Python",
    "2. Play Forza Horizon on PC",
    "3. Explore the world of UI and UX",
    "4. Build a Portfolio Website",
    "0. Exit"
]

user_input = None

while user_input != 0:
    if user_input in range(0, 5):
        print("You have chosen: {}\n".format(options[user_input - 1]))
    else:
        print("\nPlease select a valid option from the options below")
        for option in options:
            print(option)
    user_input = int(input("\nSelect an option: "))
