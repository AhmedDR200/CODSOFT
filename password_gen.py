import random

def get_password_length():
    try:
        length = int(input("Enter the desired password length: "))
        if length < 1:
            print("Please enter a positive integer for the length.")
            return get_password_length()
        return length
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return get_password_length()


def generate_password(length):

    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Password Generator")
    
    # Get desired password length from the user
    length = get_password_length()

    # Generate and display the password
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
