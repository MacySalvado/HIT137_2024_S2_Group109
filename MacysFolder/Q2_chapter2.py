def separate_and_convert(s):
    number_string = ''.join(char for char in s if char.isdigit())
    letter_string = ''.join(char for char in s if char.isalpha())

    even_numbers = [char for char in number_string if int(char) % 2 == 0]
    uppercase_letters = [char for char in letter_string if char.isupper()]

    return number_string, letter_string, even_numbers, uppercase_letters

def main():
    try:
        user_input = input("Please enter a string containing both numbers and letters: ")
        if not any(char.isdigit() for char in user_input) or not any(char.isalpha() for char in user_input):
            raise ValueError("Input must contain both numbers and letters.")

        number_string, letter_string, even_numbers, uppercase_letters = separate_and_convert(user_input)

        print(f"Original String: {user_input}")
        print(f"Number String: {number_string}")
        print(f"Letter String: {letter_string}")
        print(f"\nEven Numbers: {even_numbers}")
        print(f"Even Numbers ASCII: {[ord(char) for char in even_numbers]}")
        print(f"\nUppercase Letters: {uppercase_letters}")
        print(f"Uppercase Letters ASCII: {[ord(char) for char in uppercase_letters]}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
