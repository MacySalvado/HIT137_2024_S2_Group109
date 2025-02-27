def decrypt(text, key):
    decrypted_text = ""     # Initialise an empty string to hold the decrypted result
    for char in text:       # For loop. To loop through each character in the encrypted text
        if char.isalpha():       # Check if it's alphabet
            shifted = ord(char) - key     # Subtract the key value from the ASCII value (alternate of what we done in encryption)
            if char.islower():         # for lowercase
                if shifted < ord('a'):       # Wrap around if it's below 'a'
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):        # Wrap around if it's below 'A'
                    shifted += 26
            decrypted_text += chr(shifted)       # Convert ASCII back to character
        else:
            decrypted_text += char         # Keep non-alphabet characters the same
    return decrypted_text

# To decrypt the encrypted code
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

# Decrypt with the key and print it out
decrypted_code = decrypt(encrypted_code, 13)
print(decrypted_code)



# results of running the code, this is the decrypted code:
# yay, it works! :)
# global_variable = 100
# my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# def process_numbers():
#     global global_variable
#     local_variable = 5
#     numbers = [1, 2, 3, 4, 5]
    
#     while local_variable > 0:
#         if local_variable % 2 == 0:
#             numbers.remove(local_variable)
#         local_variable -= 1

#     return numbers

# my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
# result = process_numbers(numbers=my_set)

# def modify_dict():
#     local_variable = 10
#     my_dict['key4'] = local_variable

# modify_dict(5)

# def update_global():
#     global global_variable
#     global_variable += 10

# for i in range(5):
#     print(i)
#     i += 1

# if my_set is not None and my_dict['key4'] == 10:
#     print("Condition met!")

# if 5 not in my_dict:
#     print("5 not found in the dictionary!")

# print(global_variable)
# print(my_dict)
# print(my_dict)