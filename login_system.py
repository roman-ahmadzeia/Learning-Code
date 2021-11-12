def isLoggedIn():

    username = input(str("Enter username: "))
    password = input(str("Enter password: "))
    try:
        with open(f'{username}.txt', 'r') as file:
            for line in file:
                data = line.split(",")
                if data[0] == username and data[1] == password:
                    print("Successfully logged in")
                    return True
                else:
                    print("Wrong password or username")
                    return False

    except FileNotFoundError:
        print("Wrong Password Or Username")
        isLoggedIn()


def system():
    value = int(input("Press 1 to login Press 2 to Register: "))
    if value == 1:
        isLoggedIn()
    elif value == 2:
        username = input(str("Pick a username: "))
        password = input(str("Pick a password: "))
        with open(f"{username}.txt", "w") as file:
            file.write(f'{username},{password}')
            file.close()
            system()


system()
