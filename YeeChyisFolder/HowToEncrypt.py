def encrypt(text, key):
    encrypted_text = ""  # initialise an empty string to hold the encrypted result
    for char in text: # loop. 
        if char.isalpha(): # check if the character is alphabetic (lower/uppercase)
            shifted = ord(char) + key # calculate the new position of hte character by converting it to ASCII using ord() and add key to it.
            if char.islower(): # for lowercase
                if shifted > ord('z'): 
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

key = ????????????????
encrypted_code = encrypt(original_code, key)
print(encrypted_code)