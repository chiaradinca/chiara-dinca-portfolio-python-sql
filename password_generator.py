# Import necessary modules
import random
import string


def generate_password(length):
  # Combine letters, digits and punctuation into one character set
  characters = string.ascii_letters + string.digits + string.punctuation

  # Randomly select characters from the set to create the password
  password = ''.join(random.choice(characters) for _ in range(length))

  return password


def main():
    # Print welcome message
    print("Welcome to Password Generator")

    # Ask the user for desired password length and convert it to an integer
    length = int(input("Enter password length: "))


    # if the choosen password is too short
    if length < 4:
        print("Password should be at least 4 characters long.")
    else:
        # call generate_password and print result
        password = generate_password(length)
        print("Generated password:", password)

# This makes sure main() runs only when the script is executed directly
if __name__ == "__main__":
    main()

