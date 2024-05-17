import secrets
import string


def generate_password(name, birth_year, favorite_color, pet_name, lucky_number, favorite_food, favorite_hobby,
                      iteration=0):
    # Start with the base components of the password
    combined_word1 = favorite_food[:2].lower() + favorite_hobby[:2].lower()
    combined_word2 = favorite_hobby[:2].lower() + favorite_food[:2].lower()
    reversed_birth_year = str(birth_year)[::-1][-2:]

    if iteration % 2 == 0:
        # For even iterations, use the first letter of the name and combined_word1
        capital_letter = name[0].upper() if name else 'A'
        combined_word = combined_word1
    else:
        # For odd iterations, use the second letter of the name and combined_word2
        capital_letter = name[1].upper() if len(name) > 1 else name[0].upper()
        combined_word = combined_word2

    # Switch the numbers around
    lucky_number_str = str(lucky_number)[::-1]

    # Combine the parts
    password = (
            capital_letter +
            lucky_number_str +
            combined_word +
            reversed_birth_year
    )

    # Add additional random characters to ensure uniqueness
    additional_characters = string.ascii_letters + string.digits + string.punctuation
    while len(password) < 8:
        password += secrets.choice(additional_characters)

    # Shuffle the password to add more randomness
    password_list = list(password)
    secrets.SystemRandom().shuffle(password_list)
    shuffled_password = ''.join(password_list)

    return shuffled_password


def generate_and_display_password(name, birth_year, favorite_color, pet_name, lucky_number, favorite_food,
                                  favorite_hobby, previous_password=None, iteration=0):
    while True:
        # Generate a new password
        password = generate_password(name, birth_year, favorite_color, pet_name, lucky_number, favorite_food,
                                     favorite_hobby, iteration)

        # Modify the password if it matches the previous one
        if password != previous_password:
            break

    print("Your personalized password is:", password)
    return password
