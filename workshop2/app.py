def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")
name = input("Enter name to register: ")
pin = input("Enter PIN: ")
balance = 0
print(name + " has been registered with a starting balance of $"+str(balance))
# atm_menu(name)
while True:
    name_to_validate = input("What is your user name?")
    pin_to_validate = input("What is your user pin?")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid credentials")
        continue
while True:
    atm_menu(name)
    option = input("Choose an option:")
