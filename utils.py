def get_user_input(valid_choices):
    while True:
        choice = input("Your answer (a/b/c/d): ").lower()
        if choice in valid_choices:
            return choice
        print("Invalid input. Please choose a, b, c, or d.")
