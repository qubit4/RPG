from generation import generate_password
from encryption import encrypt
from decryption import decrypt


process = input(
    "Press 1 to generate random passwords, save them to a file, \nand optionally encrypt the file. \nPress 2 to decrypt the file. \n")

if process == "1":
    while True:
        generate_password()
        another = input("Generate another password? Yes or No: ")
        if another.lower() == "yes":
            continue
        encrypt_now = input(
            "Your passwords are now in 'document1.txt'. Encrypt the file now? Yes or No: ")
        if encrypt_now.lower() == "yes":
            encrypt("document1.txt")
            print(
                "The file is now encrypted. The encryption key is stored in 'filekey.key'.")
            break
        break
if process == "2":
    decrypt("document1.txt")
