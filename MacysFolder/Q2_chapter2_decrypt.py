def decrypt_caesar_cipher(ciphertext, shift):
    """
    Decrypts the given ciphertext using the specified shift value.
    """
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            # Shift character by the given shift value
            shifted = ord(char) - shift
            if char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                decrypted_text += chr(shifted)
            elif char.islower():
                if shifted < ord('a'):
                    shifted += 26
                decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

def find_correct_shift(ciphertext):
    """
    Tries all possible shift values and prints the decrypted message for each.
    Identifies the correct shift value that makes the message readable.
    """
    for shift in range(1, 27):
        decrypted_text = decrypt_caesar_cipher(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_text}")
        # Check if the decrypted text contains common English words
        if "the" in decrypted_text.lower() or "and" in decrypted_text.lower():
            return shift, decrypted_text
    return None, None

# Ask the user for the encrypted message
ciphertext = input("Enter the encrypted message: ")

# Find the correct shift value and the final decrypted message
correct_shift, final_decrypted_message = find_correct_shift(ciphertext)

if correct_shift:
    print(f"\nThe correct shift value is: {correct_shift}")
    print(f"The final decrypted message is: {final_decrypted_message}")
else:
    print("Could not find a readable decrypted message.")


# results of running the code and trying to input in the encrypted message provided in the question:
# it works! :)

# Shift 13: IM SELFISH IMPATIENT AND A LITTLE INSECURE I MAKE MISTAKES I AM OUT OF CONTROL ANDAT TIMES HARD TO HANDLE BUT IF YOU CANT HANDLE ME AT MY WORST THEN YOU SURE AS HELLDONT DESERVE ME AT MY BEST MARILYN MONROE

# The correct shift value is: 13
# The final decrypted message is: IM SELFISH IMPATIENT AND A LITTLE INSECURE I MAKE MISTAKES I AM OUT OF CONTROL ANDAT TIMES HARD TO HANDLE BUT IF YOU CANT HANDLE ME AT MY WORST THEN YOU SURE AS HELLDONT DESERVE ME AT MY BEST MARILYN MONROE