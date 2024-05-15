import secrets
import string


def generate_password(name, birth_year, favorite_color, pet_name, lucky_number, favorite_food, favorite_hobby):
    # Combine pet food and hobby into a single word
    combined_word = favorite_food[:2].lower() + favorite_hobby[:2].lower()


    password = (
            name[0].upper() +  # First letter of the name capitalized
            str(lucky_number) +  # Lucky number
            combined_word +  # Combined word from favorite food and hobby
            str(birth_year)[-2:]  # Last two digits of the birth year
    )

    # Add additional characters to make the password stronger
    additional_characters = string.ascii_letters + string.digits + string.punctuation
    while len(password) < 8:
        password += secrets.choice(additional_characters)

    return password


def generate_and_display_password(name, birth_year, favorite_color, pet_name, lucky_number, favorite_food,
                                  favorite_hobby, previous_password=None):
    while True:
        password = generate_password(name, birth_year, favorite_color, pet_name, lucky_number, favorite_food,
                                     favorite_hobby)
        if password != previous_password:
            break

    print("Your personalized password is:", password)
    return password


def modify_password(password, name, birth_year, lucky_number, favorite_food, favorite_hobby):
    # Modify the password based on user's request
    password = list(password)  # Convert the password to a list for easy manipulation
    password[0] = name[0].upper()  # Change the first letter to the capitalized first letter of the name
    # Switch the position of the lucky number and the year's last two digits
    password[1] = str(birth_year)[-2:]
    password[-3] = str(lucky_number)
    # Combine the last two characters into a different word
    password[-4] = favorite_food[:1].lower() + favorite_hobby[:1].lower()

    # Join the list back into a string to form the new password
    new_password = ''.join(password)
    return new_password


def main():
    print("Welcome to Personalized Password Generator!")
    name = input("What is your name? ")
    birth_year = int(input("What year were you born? "))
    favorite_color = input("What is your favorite color? ")
    pet_name = input("What is the name of your pet? ")
    lucky_number = int(input("What is your lucky number? "))
    favorite_food = input("What is your favorite food? ")
    favorite_hobby = input("What is your favorite hobby? ")

    password = generate_and_display_password(name, birth_year, favorite_color, pet_name, lucky_number, favorite_food,
                                             favorite_hobby)

    print("Reached the input prompt for generating another password.")

    while True:
        generate_again = input("Would you like to generate another password? (yes/no): ").lower()
        while generate_again not in ["yes", "no"]:
            print("Invalid input! Please enter 'yes' or 'no'.")
            generate_again = input("Would you like to generate another password? (yes/no): ").lower()

        print("User input:", generate_again)

        if generate_again == "no":
            break

        # Generate a new password with each iteration
        password = generate_and_display_password(name, birth_year, favorite_color, pet_name, lucky_number,
                                                 favorite_food, favorite_hobby, password)


if __name__ == "__main__":
    main()
