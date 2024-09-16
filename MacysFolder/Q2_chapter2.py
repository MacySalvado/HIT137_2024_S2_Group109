def separate_and_convert(s):
    number_string = ''.join([char for char in s if char.isdigit()])
    letter_string = ''.join([char for char in s if char.isalpha()])

    # Convert even numbers to ASCII code decimal values
    even_numbers = [char for char in number_string if int(char) % 2 == 0]
    even_numbers_ascii = [ord(char) for char in even_numbers]
    converted_numbers = ''.join([str(ord(char)) if int(char) % 2 == 0 else char for char in number_string])

    # Convert uppercase letters to ASCII code decimal values
    uppercase_letters = [char for char in letter_string if char.isupper()]
    uppercase_letters_ascii = [ord(char) for char in uppercase_letters]
    converted_letters = ''.join([str(ord(char)) if char.isupper() else char for char in letter_string])

    return number_string, letter_string, converted_numbers, converted_letters, even_numbers, even_numbers_ascii, uppercase_letters, uppercase_letters_ascii

# Prompt the user for input
user_input = input("Please enter a string containing both numbers and letters: ")

# Process the user input
number_string, letter_string, converted_numbers, converted_letters, even_numbers, even_numbers_ascii, uppercase_letters, uppercase_letters_ascii = separate_and_convert(user_input)

# Display the results
print(f"Original String: {user_input}")
print(f"Number String: {number_string}")
print(f"Letter String: {letter_string}")
print("\nSummary of Even Numbers and their ASCII Codes:")
print(f"Even Numbers: {even_numbers}")
print(f"Even Numbers converted to ASCII code: {even_numbers_ascii}")
print("\nSummary of Uppercase Letters and their ASCII Code:")
print(f"Uppercase Letters: {uppercase_letters}")
print(f"Uppercase Letters converted to ASCII Code: {uppercase_letters_ascii}")
