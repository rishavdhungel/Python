#!/usr/bin/python
from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import csv
try:
    from prettytable import from_csv
    from prettytable import PrettyTable
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", 'prettytable'])

def ask():
    print('''
    
    1._____________________       2._________________
      |       LOG IN       |        |    SIGN UP     |
      |____________________|        |________________|
          ''')
    choice = input("Choose Your Option (1/2): ")
    if choice == "1":
        menu()
    if choice == "2":
        register()
    else:
        print("Invalid Input: ")
        ask()




def menu():
    name = str(input("Enter a Username: "))
    password = str(input("Enter a password: "))
    with open('info.csv', 'r+') as csv_file:
        csvreader = csv.reader(csv_file)
        for row in csvreader:
            first = name
            second = password
            if row[2] == first and row[4]== second:
                    message = "Hi! %s you are logged in" % name + """\n 

                      ------------------------------------------------------------------
                     |==================================================================| 
                     |======== Welcome To Car Dealership Management Software ===========|
                     |==================================================================|
                      ------------------------------------------------------------------
                 1.Buy 
                 2.Sell
                 3.Search
                 4.Show all
                 5.Quit
                       """
                    print(message)
                    calculation()
        else:
            check()


def calculation():
    task = int(input("Enter a Option: "))
    if (task) == 1:
        print("You Have Selected Option (Buy)")
        buy()
    if (task) == 2:
        print("You Have Selected Option (Sell)")
        sell()
    if (task) == 3:
        print("You Have Selected Option (Search)")
        search_car()
    if (task) == 4:
        print("You Have Selected Option (Show All)")
        show_all()
    if (task) == 5:
        print("You Have Selected Option (Quit)")
        print("Terminating The Process ..... ..")
        exit(0)
    else:
        print("Invalid option! The Input must be between 1 to 5")
        msg()
def msg():
    message = "Please Select The Right Option!: " + """
         1.Buy 
         2.Sell
         3.Search
         4.Show all
         5.Quit
               """
    print(message)
    calculation()


def try_again():
    option = input("Do you want to return to main menu (Y/N): ")
    if option == "y":
        msg()
    else:
        print("You Have Selected Option (Quit)")
        print("Terminating The Process ..... ..")
        exit(0)
def buy():
    fieldnames = [ 'Model', 'Rego', 'Color', 'Price']
    with open ('data.csv', 'a') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        Model = input("Enter a Model of a Car: ")
        Rego = input("Enter a Registration No(Rego): ")
        Color = input("Enter a Color of a Car: ")
        Price = float(input("Enter a Price of a Car: "))
        writer.writerow({
                "Model": Model,
                "Rego":Rego,
                "Color":Color,
                "Price":Price
            })
        csv_file.close()
        try_again()
def sell():
    csvfile = open("data.csv")
    x = from_csv(csvfile)
    print(x)
    lines = list()
    with open('data.csv', 'r') as readFile:
        name = input("Please enter Rego of a car to sell:")
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == name:
                    lines.remove(row)
    with open('data.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
        try_again()
        csvfile.close()
        readFile.close()
def search_car():
    with open('data.csv','r+') as csvfile:
        name = str(input('Enter the Model to search : '))
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row[0]==name:
                table = PrettyTable(row)
                print(table)
        else:
            print("No such model found in Database:")
            try_again()

def show_all():
   csvfile = open("data.csv")
   x = from_csv(csvfile)
   print(x)
   csvfile.close()
   try_again()

def check():
        print("Wrong Username or Password! \n Please try again!")
        menu()
def register():
    print("Thank You!! For Choosing Us ")
    fieldnames = ['firstname', 'lastname','username', 'email', 'password']
    with open('info.csv', 'a') as  csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        firstname = input("Enter your first name")
        lastname = input("Enter your last name")
        username = input("Enter a username: ")
        email = input("Enter Your email address:")
        newpassword = input("Set a  new password")
        verify = input("Re enter a password")

        if newpassword == str(verify):
            writer.writerow({
                        "firstname": firstname,
                        "lastname": lastname,
                        "username": username,
                        "email": email,
                        "password": newpassword
                    })

        else:
                    print("The Password you input does not match")
                    print("Try Again")
                    register()




ask()
