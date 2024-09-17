def decrypt(text, key):
    decrypted_text = ""  # Initialise an empty string for the decrypted text
    for char in text:  # Loop through each character in the encrypted text
        if char.isalpha():  # Check if it's an alphabetic character
            shifted = ord(char) - key  # Subtract the key value from the ASCII value
            if char.islower():
                if shifted < ord('a'):  # Wrap around if it's below 'a'
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):  # Wrap around if it's below 'A'
                    shifted += 26
            decrypted_text += chr(shifted)  # Convert ASCII back to character
        else:
            decrypted_text += char  # Keep non-alphabet characters the same
    return decrypted_text

# Now decrypt the encrypted code you provided
encrypted_code = """tybony_inevnoyr = 100
zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}

qrs cebprff_ahzoref():
    tybony tybony_inevnoyr
    ybpny_inevnoyr = 5
    ahzoref = [1, 2, 3, 4, 5]
    
    juvyr ybpny_inevnoyr > 0:
        vs ybpny_inevnoyr % 2 == 0:
            ahzoref.erzbir(ybpny_inevnoyr)
        ybpny_inevnoyr -= 1
        
    erghea ahzoref
    
zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg = cebprff_ahzoref(ahzoref=zl_frg)

qrs zbqvsl_qvpg():
    ybpny_inevnoyr = 10
    zl_qvpg['xrl4'] = ybpny_inevnoyr

zbqvsl_qvpg(5)

qrs hcqngr_tybony():
    tybony tybony_inevnoyr
    tybony_inevnoyr += 10

sbe v va enatr(5):
    cevag(v)
    v += 1

vs zl_frg vf abg Abar naq zl_qvpg['xrl4'] == 10:
    cevag("Pbaqvgvba zrg!")

vs 5 abg va zl_qvpg:
    cevag("5 abg sbhaq va gur qvpgvbanel!")

cevag(tybony_inevnoyr)
cevag(zl_qvpg)
cevag(zl_qvpg)
"""

# Decrypt using the key
decrypted_code = decrypt(encrypted_code, 13)
print(decrypted_code)