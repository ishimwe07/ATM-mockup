database = {}

print("Welocome to the bank PYTHON.")


def init():
    print("Do you have an account with us?")
    print("1. yes")
    print("2. no")
    
    haveAccount = int(input("please select an option: \n"))

    if(haveAccount == 1):
        login()
        
    elif(haveAccount == 2):
        register()
        
    else:
        print("Invalid option, Please try again.")
        init()


def generatingAccountNumber():
    
    import random
    return random.randrange(000000000000,999999999999)
    


def register():
    print("****** REGISTER ********")
    firstName = input("What is your first name? \n")
    lastName = input("What is your last name? \n")
    email = input("What is your Email \n")
    password = input("Create your password \n")
    accountNumber = generatingAccountNumber()

    database[accountNumber] = [ firstName, lastName, email, password ]
    
    print("Welcome!, Your Account has been created.")
    print("And your account number is %d" %accountNumber)

    login()
 
   
def login():
    print("Login to your Account:")
    accountNumberFromUser = int(input("Enter your account number: \n"))

    
    for accountNumber, userDetails in database.items():
        if(accountNumberFromUser == accountNumber):

            password = input("Enter your password: \n")
            
            if(password == userDetails[3]):

                print("Welcome %s %s." %(userDetails[0], userDetails[1]))

                bankOps(userDetails)
            else:
                print("Invalid password, Please try again ")
                login()
           
        else:
            print("Invalid Account Number, please try again ")
            login()

    

    
def bankOps(user):
    
    selectedOption = int(input("What would you like to do: (1) Deposit (2) Withdrawal (3)Logout (4) Exit \n"))

    if(selectedOption == 1):
        depositOperation()
        
    elif(selectedOption == 2):
        withdrawalOperation()
        
    elif(selectedOption == 3):
        login()
        
    elif(selectedOption == 4):
        exit()

    else:
        print("Invalid option selected, Please try again ")

        bankOps(user)
        
def withdrawalOperation():
    withdrawal = int(input("How much would you like to withdraw? \n"))
    print("Take your cash.")
    

    
def depositOperation():
    Deposit = int(input("How much would you like to deposit? \n"))
    print("Your new balance is %d" %Deposit)


init()

