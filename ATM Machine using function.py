# Initialize global variables
password = 4567
amount = 2000

def initial():
    print("Welcome to my ATM Machine")
    pin = int(input("Enter the Pin: "))
    if pin == password:
        print("Press 1 for change password")
        print("Press 2 for checking Balance")
        print("Press 3 for debit")
        print("Press 4 for credit")
        print("Press 5 to exit")
        choice = int(input("Enter the choice: "))
        if choice == 1:
            change_password()
        elif choice == 2:
            check_balance()
        elif choice == 3:
            debit()
        elif choice == 4:
            credit()
        else:
            print("Thank You")
    else:
        print("Incorrect Password")
        initial()

def check_balance():
    print("Your current balance is", amount)
    initial()
    
def debit():
    global amount
    takeaway = int(input("Enter the amount to debit: "))
    if takeaway > amount:
        print("Insufficient balance")
    else:
        amount -= takeaway
        print("Your amount is debited successfully")
        print("Your new amount is: ", amount)
    initial()
    
def credit():
    global amount
    credit_amount = int(input("Enter the amount you want to credit: "))
    amount += credit_amount
    print("Your new balance is:", amount)
    initial()

def change_password():
    global password
    old = int(input("Enter the old password: "))
    if old == password:
        newpin = int(input("Enter the new password: "))
        password = newpin
        print("Password changed successfully!")
    else:
        print("Invalid password")
    initial()

initial()
