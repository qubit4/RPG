def generate_password():
    import random
    import string

    account = input("Enter the account name: ")
    number = int(input("Number of characters in password? "))

    random_password = ("".join(random.choices(
        string.ascii_letters + string.digits, k=number)))

    with open("document1.txt", "a") as doc:
        doc.write(account + " | " + random_password + "\n")
