#Programmer: Sarah Darwiche
#Description: BankApp
#Date: 5/29/2023

global balance, username, password, loggedInUser
balances = [] 
userName = [] 
passWord = [] 
loggedInUser = ""


def readInputFromFile():
    file = open("UserInformation.txt", "r")
    for i in file:
        lineItem = i.split()
        print(lineItem)
        
        userName.append(lineItem[0])
        passWord.append(lineItem[1])
        balances.append(float(lineItem[2]))
    
    print("balances: ", balances)
    print("userName: ", userName)
    print("passWord: ", passWord)
    
    file.close()

def writeUpdatestoFile():
    file = open("UserInformation.txt", "w")
  
    for j in range(len(userName) - 1):
        file.write(userName[j] + " ") 
        file.write(passWord[j]+ " ") 
        file.write(str(balances[j]) + "\n") 
    
    file.write(userName[j+1] + " ") 
    file.write(passWord[j+1]+ " ") 
    file.write(str(balances[j+1])) #don't add an extra line in the file
      
    file.close()

def showBalance():
    index = userName.index(loggedInUser)
    balance = balances[index]
    print("Your balance is ", balance)

def addNewUser():
    newUser = input("Please eneter your username: ")
    userName.append(newUser)
    newPassword = input("Please enter your password: ")
    passWord.append(newPassword)
    newBalance = float(input("Please enter your balance: "))
    balances.append(newBalance)

    print ("balances: ", balances)
    print("userName: ", userName)
    print("passWord: ", passWord)

def changeUser(username):
    global loggedInUser
    try:
        index = userName.index(username)
    except ValueError as ve:
        print("Your username is invalid. Goodbye.")
        exit()
    try:
        password = input("Please enter your password: ")
        if passWord[index] != password:
            print("Your password is invalid. Goodbye.")
            exit()
    except ValueError as ve:
        print("Your password is invalid. Goodbye.")
        exit()
    
    loggedInUser = username
    print("You are now logged in as ", loggedInUser)


def userInputValidation(string):
    while True:
        try:
            option = float(input(string))
            while(option <=0) :
                print("option value should be > 0")
                option = float(input(string))
            break
        except:
            print("Letters are not valid... please try again")
            
    return option

def deposit(amount):
    index = userName.index(loggedInUser)
    balances[index] = balances[index] + amount
    print("You have deposited ", amount)

def withdraw(amount):
    index = userName.index(loggedInUser)
    if balances[index] >= amount:
        balances[index] = balances[index] - amount
        print("You have withdrawn ", amount)
    else:
        print("You do not have enough money in your account to withdraw.")

def validateUserInformation():
    global loggedInUser
    username = input("Please enter your username: ")
    try:
        index = userName.index(username)
    except ValueError as ve:
        print("Your username is invalid. Goodbye.")
        exit()
    try: 
        password = input("Please enter your password: ")
        if passWord[index] != password:
            print("Your password is invalid. Goodbye.")
            exit()
    except ValueError as ve:
        print("Your password is invalid. Goodbye.")
        exit()
   
    loggedInUser = username
    print("login sucess!")


def menu(): 
    KeepGoing = "yes"
    while KeepGoing == "yes":
    
        print("\n Welcome to the bank app")
        print("Please select from the following options\n")

        print("Type D to deposit money")
        print("Type W to withdraw money")
        print("Type C to change user, display username")
        print("Type A to add new client")
        print("Type E to exit \n")

        menuSelection = input("\nEnter your menu selection \n")

        if (menuSelection == "D"):
            print("You have decided to deposit money")

            depositAmount = float(userInputValidation("How much would you like to deposit? "))
            deposit(depositAmount)
            showBalance()

        elif (menuSelection == "W"):
            print("You have decided to withdraw money")
            withdrawAmount = float(userInputValidation("How much would you like to withdraw? "))
            showBalance()
            withdraw(withdrawAmount)
            showBalance()

        elif (menuSelection == "B"):
            print("You have decided to view balance")
            showBalance()

        elif (menuSelection == "C"):
            print("You have decided to change user")
            username = input("Please enter your username: ")
            changeUser(username)

        elif (menuSelection == "A"):
            print("You have decided to add a new client")
            addNewUser()
     
        elif (menuSelection == "E"):
            print("You have decided to quit the program. Goodbye.")
            writeUpdatestoFile()
            exit()

        else:
            print("You have selected an invalid menu option. Please try again.")


def main():
    readInputFromFile()
    validateUserInformation()
    menu()
    
main()