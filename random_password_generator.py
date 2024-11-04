import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    """Generate a random password based on user-defined criteria."""
    character_set = ''
    
    if use_letters:
        character_set += string.ascii_letters  # Add letters (both lowercase and uppercase)
    if use_numbers:
        character_set += string.digits         # Add digits (0-9)
    if use_symbols:
        character_set += string.punctuation     # Add symbols

    if not character_set:
        raise ValueError("At least one character type must be selected.")
    
    # Generate the password
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Get user preferences
    length = int(input("Enter the desired password length: "))
    
    use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    try:
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"\nGenerated Password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
