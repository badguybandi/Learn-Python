from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            acc_name, username, password = data.split("|")
            print("Account:", acc_name, "|Username:", username, "|Password:", fer.decrypt(password.encode()).decode())

def add():
    name = input("Account Name: ")
    username = input("Username: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + username + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
        

master_pwd = input("What is the master password?")
key = load_key()
fer = Fernet(key)

while True:
    mode = input("Would you like to add a new password or view existing ones (view,add)?Press q to quit ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode!")
        continue

  