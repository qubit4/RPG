from cryptography.fernet import Fernet


def decrypt(filename):

    with open("filekey.key", "rb") as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    with open(filename, "rb") as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(filename, "wb") as dec_file:
        dec_file.write(decrypted)
