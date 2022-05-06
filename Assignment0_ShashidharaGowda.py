import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def check(email):
    if (re.fullmatch(regex, email)):
        return "Valid"
    else:
        return "InValid"


def password_check(passwd):
    SpecialSym = "!@#$%^&*<>?"
    val = True

    if len(passwd) < 5:
        print('length should be at least 6')
        val = False

    if len(passwd) > 16:
        print('length should be not be greater than 8')
        val = False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of special character')
        val = False
    if val:
        return val

def register():
    email=input("Enter the email address\n")
    if check(email)=='InValid':
        print("The entered email address is invalid\n Please retry\n\n")
        mainMethod()
    password=input("Enter the password\n")
    while not password_check(password):
        password=input("Enter the password\n")
    creds=open("Credentials.txt",'a')
    creds.write("{}|{}\n".format(email,password))
    creds.close()
    print("{} is Succesfully Registered".format(email))
    mainMethod()

def login():
    creds=open('Credentials.txt','r')
    data=creds.readlines()
    user_creds={}
    for i in data:
        if '|' in i:
            i=i.split('|')
            user_creds[i[0]]=i[1]


    email=input("Enter email address to login\n")

    if email in user_creds:
        password=input("Enter the password\n")
        if password==user_creds[email]:
            print("Succesfully logged in!!")
        else:
            temp=input("password is not matching, Please select the following\n1. MainMenu \n2.forget password \n")
            if temp=='1':
                mainMethod()
            elif temp=='2':
                print("Please find your password below\n{}".format(user_creds[email]))
                mainMethod()
    else:
        print("Unable to locate the email in our system, Please register\n")
        mainMethod()
def mainMethod():
    a = input("Enter\n 1 to Register\n 2 to Login\n3 to Exit\n")
    if a == '1':
        register()
    elif a == '2':
        login()
    else:
        exit()
mainMethod()

