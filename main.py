from password_generator import generate_and_display_password

if __name__ == "__main__":
    print("Welcome to Personalized Password Generator!")
    name = input("What is your name? ")
    birth_year = int(input("What year were you born? "))
    favorite_color = input("What is your favorite color? ")
    pet_name = input("What is the name of your pet? ")
    lucky_number = int(input("What is your lucky number? "))
    favorite_food = input("What is your favorite food? ")
    favorite_hobby = input("What is your favorite hobby? ")

    # Generate and display the initial password
    password = generate_and_display_password(name, birth_year, favorite_color, pet_name, lucky_number, favorite_food,
                                             favorite_hobby)

    print("Reached the input prompt for generating another password.")

    iteration = 1

    while True:
        generate_again = input("Would you like to generate another password? (yes/no): ").lower()
        while generate_again not in ["yes", "no"]:
            print("Invalid input! Please enter 'yes' or 'no'.")
            generate_again = input("Would you like to generate another password? (yes/no): ").lower()

        print("User input:", generate_again)

        if generate_again == "no":
            break

        # Generate and display a new password, passing the previous password and iteration count
        password = generate_and_display_password(name, birth_year, favorite_color, pet_name, lucky_number,
                                                 favorite_food, favorite_hobby, password, iteration)
        iteration += 1
