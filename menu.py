from files_handler import save_to_file, read_from_file
from rc4 import encrypt, decrypt

plaintext_file_name = "./files/plaintext.txt"
ciphertext_file_name = "./files/ciphertext.txt"

def encrypt_menu():
    print("\nEncryption")
    print("1 - to read text from file")
    print("2 - to read text from console")
    print("0 - Back")

    choice = input()
    match(choice):
        case "1":
            plaintext = read_from_file(plaintext_file_name)
        case "2":
            plaintext = input(str('Enter your plaintext: '))
        case "0":
            return main_menu()
    
    key = input(str('Enter your secret key: '))
    ciphertext = encrypt(plaintext, key)

    choice = input("Save result to file y/n?")
    if choice.upper() == "Y":
        save_to_file(ciphertext_file_name, ciphertext)

    print("\nResult:")
    print(ciphertext)


def decrypt_menu():
    print("\nDecryption")
    print("1 - to read ciphertext from file")
    print("2 - to read ciphertext from console")
    print("0 - Back")

    choice = input()
    match(choice):
        case "1":
            ciphertext = read_from_file(ciphertext_file_name)
        case "2":
            ciphertext = input(str('Enter your ciphertext: '))
        case "0":
            return main_menu()
    
    key = input(str('Enter your secret key: '))
    plaintext = decrypt(ciphertext, key)

    choice = input("Save result to file y/n?")
    if choice.upper() == "Y":
        save_to_file(plaintext_file_name, plaintext)

    print("\nResult:")
    print(plaintext)

def main_menu():
    print("\nRC-4")
    choice = input('E - Encrypt \nD - Decrypt\n').upper()
    match(choice):
        case "E": 
            encrypt_menu()
        case "D":
            decrypt_menu()
        case _:
            print("Invalid value!")