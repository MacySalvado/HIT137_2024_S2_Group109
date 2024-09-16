def separate_and_convert(s):
    # extract numbers and letters from the input string
    number_string = ''.join(char for char in s if char.isdigit())
    letter_string = ''.join(char for char in s if char.isalpha())

    # find the even numbers and uppercase letters from string
    even_numbers = [char for char in number_string if int(char) % 2 == 0]
    uppercase_letters = [char for char in letter_string if char.isupper()]

    # return the extracted and converted values
    return number_string, letter_string, even_numbers, uppercase_letters

def main():
    # ask the user for input
    user_input = input("Please enter a string containing both numbers and letters: ")

    # process the user input
    number_string, letter_string, even_numbers, uppercase_letters = separate_and_convert(user_input)

    # display the results
    print(f"Original String: {user_input}")
    print(f"Number String: {number_string}")
    print(f"Letter String: {letter_string}")
    print(f"\nEven Numbers: {even_numbers}")
    print(f"Even Numbers ASCII: {[ord(char) for char in even_numbers]}")
    print(f"\nUppercase Letters: {uppercase_letters}")
    print(f"Uppercase Letters ASCII: {[ord(char) for char in uppercase_letters]}")

# ensures that the main function runs only when the script is executed directly
if __name__ == "__main__":
    main()
