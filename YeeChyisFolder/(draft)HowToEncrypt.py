# This is just a DRAFT




def encrypt(text, key):
    encrypted_text = ""    # initialise an empty string to hold the encrypted result
    for char in text:   # for loop. 
        if char.isalpha():   # check if the character is alphabetic (lower/uppercase)
            shifted = ord(char) + key   # calculate the new position of the character by converting it to ASCII using ord() and add key to it.
            if char.islower():   # for lowercase
                if shifted > ord('z'): 
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():    # for uppercase
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text