def Database():
    global database
    database=dict()

def start():
    choice=input("Press L for login or S for Sign up: ")
    if choice=="L":
        login()
    elif choice=="S":
        signup()
    else:
        print("Wrong Input Given")

def signup():
    email=input("Enter the email to sign up: ")
    password=input("Enter the password: ")
    # check=prishu.ask_password()
    # database.update(email,password)
    # print(database)
    database[email]=password
    print("Signed up successfully")
    start()

def login():
    # Database()
    global database
    email=input("Enter the email to login: ")
    pass_=input("Enter the pass_: ")
    if email in database:
        if database[email]==pass_:
            print("Log in Successfully")
        else:
            print("Incorrect Password")
    else:
        print("You have'nt sign up yet")
        print("Sign up first")
        signup()
Database()
start()