# Antonio Rios
# January 23, 2015
# CS136 Lab
# Lab1: Caesar Cipher Implementation
#====================================


def encrypt_char(char, key):
    """
    :param char: The character to be encrypted using a Caesar Cipher. A string of length 1.
    :param key: The key used to encrypt char. An int.
    :return: The encrypted character. A string of length 1.
    """
    if char.islower():
        base = 96
    elif char.isupper():
        base = 64
    else:
        return char
    new_char = ord(char) + key - base
    while new_char > 26:
        new_char -= 26
    return chr(new_char + base)

def encrypt_string(s, key):
    """
    :param s: The string to be encrypted using a Caesar Cipher. A string.
    :param key: The key used to encrypt str. An int.
    :return: The encrypted string. A string.
    """
    new_s = ''
    for c in s:
        new_s += encrypt_char(c, key)
    return new_s

def decrypt_string(s, key):
    """
    :param s: The string to be decrypted using a Caesar Cipher. A string.
    :param key: The key used to decrypt str. An int.
    :return: The decrypted string. A string.
    """
    return encrypt_string(s, 26-key)

def interactive():
    print("Welcome to the Caesar Cipher program!")
    while True:
        print()
        print("Enter: -- \"e\" to encrypt a file")
        print("       -- \"d\" to decrypt a file")
        print("       -- \"c\" to crack a file")
        choice_1 = input("Your choice: ")
        print()
        if choice_1 == 'e' or choice_1 == 'd' or choice_1 == 'c':
            break
        print("Sorry. Choice has to be \"e\", \"d\", or \"c\".")
    if choice_1 == "e":
        while True:
            print("Enter the name of the file to encrypt:")
            file_name = input("File name: ")
            file = open(file_name, 'r') ############################## Handle exception
            print()
            break
        while True:
            print("Enter the shift to be used in the encryption:")
            shift = int(input("Shift entered: "))
            print()
            if type(shift) == int:
                break
            print("Please enter an integer.")
            print()
        while True:
            print("Enter the name of the file to store the encrypted result:")
            output_name = input("File name: ")
            out = open(output_name, 'w')
            print()
            break
        print("Encrypting file " + file_name + " with a shift of " +
              str(shift) + " and storing the results in " + output_name)
        plaintext = file.read()
        file.close()
        ciphertext = encrypt_string(plaintext, shift)
        out.write(ciphertext)
        out.close()
        print()
        print("All done! encryption is complete.")
    elif choice_1 == 'd':
        while True:
            print("Enter the name of the file to decrypt:")
            file_name = input("File name: ")
            file = open(file_name, 'r') ############################## Handle exception
            print()
            break
        while True:
            print("Enter the shift to be used in the decryption:")
            shift = int(input("Shift entered: "))
            print()
            if type(shift) == int:
                break
            print("Please enter an integer.")
            print()
        while True:
            print("Enter the name of the file to store the decrypted result:")
            output_name = input("File name: ")
            out = open(output_name, 'w')
            print()
            break
        print("Decrypting file " + file_name + " with a shift of " +
              str(shift) + " and storing the results in " + output_name)
        ciphertext = file.read()
        file.close()
        plaintext = decrypt_string(ciphertext, shift)
        out.write(plaintext)
        out.close()
        print()
        print("All done! decryption is complete.")
    elif choice_1 == 'c':
        while True:
            print("Enter the name of the file to crack:")
            file_name = input("File name: ")
            file = open(file_name, 'r') ############################## Handle exception
            print()
            break
        while True:
            print("Enter the name of the file to append the cracked results to:")
            output_name = input("File name: ")
            out = open(output_name, 'a')
            print()
            break
        print("Cracking file " + file_name + " and storing the results in " + output_name)
        ciphertext = file.read()
        for i in range(26):
            out.write("With a shift of " + str(i) + ":\n")
            out.write(decrypt_string(ciphertext, i) + '\n')
        file.close()
        out.close()
        print()
        print("All done! cracking is complete.")




interactive()

#key = 4
#print(decrypt_string(encrypt_string('The quick brown fox jumps over the lazy dog. 42', key), key))
