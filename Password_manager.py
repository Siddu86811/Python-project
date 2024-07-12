from cryptography.fernet import Fernet

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip()
            user, passw = data.split('|')
            print('user:', user, '| password:', fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account name: ')
    pwd = input('Password: ')

    with open('password.txt', 'a') as f:
        f.write('name' + '|' + fer.encrypt(pwd.encode()).decode() + '\n')


while True:
    master = input('Do you want to log in, Enter view/add or q to quit.')
    if master == 'q':
        break
    if master == 'view':
        view()
    elif master == 'add':
        add()
    else:
        print('invalid.')
        continue
