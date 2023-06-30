def show_balance(balance):
    print("Your account balance is: $" + str(balance))


def deposit(balance):
    amount = input("Enter an amount to deposit: ")
    return float(amount) + balance


def withdraw(balance):
    withdrawal = input("Enter an amount to withdraw: ")
    return balance - float(withdrawal)


def logout(name):
    print("Goodbye "+ name)