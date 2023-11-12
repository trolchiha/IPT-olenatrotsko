from rc4_implementation.rc4 import RC4
from rc4_implementation.file_handler import save_to_file, read_from_file

class RC4_menu:
    def __init__(self, plaintext_file_name="plaintext.txt", ciphertext_file_name="ciphertext.txt"):
        self.plaintext_file_name = "./text_files/" + plaintext_file_name
        self.ciphertext_file_name = "./text_files/" + ciphertext_file_name
        self.RC4 = None
     
    def main_menu(self):
        print("\nRC-4")
        choice = input('E - Encrypt \nD - Decrypt\n').upper()
        match(choice):
            case "E": 
                print("\nEncryption")
                plaintext, key = self.sub_menu(self.plaintext_file_name)
                self.RC4 = RC4(key, plaintext, None)
                self.RC4.encrypt()
                self.save_menu(self.ciphertext_file_name, self.RC4.get_ciphertext())
            case "D":
                print("\nDecryption")
                ciphertext, key = self.sub_menu(self.ciphertext_file_name)
                self.RC4 = RC4(key, None, ciphertext)
                self.RC4.decrypt()
                self.save_menu(self.plaintext_file_name, self.RC4.get_plaintext())
            case _:
                print("Invalid value!")
        
    def sub_menu(self, read_file):
        print("1 - to read text from file")
        print("2 - to read text from console")
        print("0 - Back")

        choice = input()
        match(choice):
            case "1":
                text = read_from_file(read_file)
            case "2":
                text = input(str('Enter your text: '))
            case "0":
                return self.main_menu()
        
        key = input(str('Enter your secret key: '))

        return text, key

    def save_menu(self, save_file, result):
        choice = input("Save result to file y/n?")
        if choice.upper() == "Y":
            save_to_file(save_file, result)

        print("\nResult:")
        print(result)
