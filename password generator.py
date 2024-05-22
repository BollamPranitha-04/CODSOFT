import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_punctuation=True):
    # Define the character sets to be used in the password
    char_set = string.ascii_lowercase
    if use_uppercase:
        char_set += string.ascii_uppercase
    if use_digits:
        char_set += string.digits
    if use_punctuation:
        char_set += string.punctuation

    # Ensure there is at least one character type in the set
    if not char_set:
        raise ValueError("No character sets selected for password generation.")

    # Generate the password
    password = ''.join(random.choice(char_set) for _ in range(length))

    return password

# Example usage
length = 12  # You can change the length as needed
password = generate_password(length)
print(f"Generated password: {password}")
