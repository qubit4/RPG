def encrypt(filename):
    from cryptography.fernet import Fernet

    key = Fernet.generate_key()

    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)

    fernet = Fernet(key)

    with open(filename, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(filename, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
