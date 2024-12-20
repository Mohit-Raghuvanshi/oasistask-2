import random
import string

def generate_password(length, use_letters, use_digits, use_symbols):
    char_pool = ""
    if use_letters:
        char_pool += string.ascii_letters
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        raise ValueError("At least one character set must be selected.")

    return "".join(random.choice(char_pool) for _ in range(length))

def main():
    print("Random Password Generator")
    try:
        length = int(input("Enter password length: "))
        use_letters = input("Include letters? (y/n): ").strip().lower() == "y"
        use_digits = input("Include digits? (y/n): ").strip().lower() == "y"
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == "y"

        password = generate_password(length, use_letters, use_digits, use_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
