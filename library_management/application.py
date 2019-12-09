#!/usr/bin/python
import csv
import subprocess
import sys
#install pip on your device before runniv=ng program
#the program uses module Prettytable so automatically installing it when program start
try:
    from prettytable import from_csv
    from prettytable import PrettyTable
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", 'prettytable'])

#Asking user for login and signup
def ask():    #info.csv file stores the credientials for logins new user has to signup
    print('''
    
    1. ...................      2 ...................
      |      LOG IN       |        |    SIGN UP      |
      |...................|        |.................|
          ''')
    choice = input("Choose Your Option (1/2): ")
    if choice == "1":
        menu()
    if choice == "2":
        register()
    else:
        print("Invalid Input: ")
        ask()


#main menu
def menu():
    name = str(input("Enter a Username: "))
    password = str(input("Enter a password: "))
    with open('info.csv', 'r+') as csv_file: #info.csv file stores the credientials for logins new user has to signup
        csvreader = csv.reader(csv_file)
        for row in csvreader:
            first = name
            second = password
            if row[2] == first and row[4]== second:
                    message = "Hi! %s you are logged in" % name + """\n 

                      ------------------------------------------------------------------
                     |======================KATHMANDU UNIVERSITY========================| 
                     |========== Welcome To  Library Management System =================|
                     |==================================================================|
                      ------------------------LIBRARY MENU-------------------------------
                 1.Add New Books To The Record
                 2.Issue  Books 
                 3.Search a Book
                 4.Return a Book
                 5.Request Books  
                 6.Display all available Books
                 7:Display all requested Books
                 8.Exit
                       """
                    print(message) # the request books are to be stored in a new csv files (request.csv)
                    calculation()
        else:
            check()

#processing the selected options
def calculation():
    task = int(input("Enter a Option: "))
    if (task) == 1:
        print("You Have Selected Option (Add New Books To The Record)")
        add()
    if (task) == 2:
        print("You Have Selected Option (Issue  Books )")
        issue()
    if (task) == 3:
        print("You Have Selected Option (Search)")
        search()
    if (task) == 4:
        print("You Have Selected Option (Return a Book)")
        add()
    if (task) == 5:
        print("You Have Selected Option (Request Books )")
        request()
    if (task) == 6:
        print("You Have Selected Option (Display all available books)")
        show_all()
    if (task) == 7:
        print("You Have Selected Option (Display all requested Books)")
        show_request()

    if (task) == 8:
        print("You Have Selected Option (Quit)")
        print("Terminating The Process ..... ..")
        exit(0)
    else:
        print("Invalid option! The Input must be between 1 to 8")
        msg()
def msg():
    message = "Please Select The Right Option!: " + """
                 1.Add New Books To The Record
                 2.Issue  Books 
                 3.Search a Book
                 4.Return a Book
                 5.Request Books  
                 6.Display all available Books
                 7:Display all requested Books
                 8.Exit
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
        exit()
#we are using  csv file handling to store the data on our record so it will be more convinent
#adding the books to record
def add():
    fieldnames = [ 'Name', 'Registration', 'ISBN']
    with open ('data.csv', 'a+') as csv_file:#a,a+ is needed dont use w,w+ as it overwrites the data
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        Name = input("Enter a Name of a Book: ")
        Rego = input("Enter a Registration No: ")
        ISBN = input("Enter a ISBN No.:  ")
        writer.writerow({
                "Name": Name,
                "Registration":Rego,
                "ISBN":ISBN,

            })
        csv_file.close()#closing the csv file to manage memory
        try_again()#asking the user to chose to go to main menue or not
#issuing book and removing book from record
def issue():
    csvfile = open("data.csv")
    x = from_csv(csvfile)
    print(x)
    lines = list()#converting csv data to list and then rewriting back to csv file after change
    with open('data.csv', 'r') as readFile:
        name = input("Please enter Registration No of the Book :")
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == name:
                    lines.remove(row)
    with open('data.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
        csvfile.close()
        readFile.close()
        try_again()
#Implementing search option for Books
def search():
    with open('data.csv','r+') as csvfile:
        name = str(input('Enter the Name to search : '))
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row[0]==name:
                table = PrettyTable(row)
                print(table)
        else:
            print("No such Book found in Database:")
            try_again()
#Request new book and store it saperately in another csv file
def request():
    fieldnames = ['Name', 'Author', 'Edition']
    with open ('request.csv', 'a+') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        Name = input("Enter a Name of a Book: ")
        Author = input("Enter a Author of the Book ")
        Edition = input("Enter a Edition of Book: ")
        writer.writerow({
                "Name": Name,
                "Author": Author,
                "Edition": Edition,


            })
        csv_file.close()
        try_again()
#showing the data on table form
def show_all():
   csvfile = open("data.csv")
   x = from_csv(csvfile)
   print(x)
   csvfile.close()
   try_again()
#showing the data of the request section
def show_request():
   csvfile = open("request.csv")
   x = from_csv(csvfile)
   print(x)
   csvfile.close()
   try_again()

#Registration process
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
#Cchecking for verification
def check():
    print("Wrong Username or Password! \n Please try again!")
    menu()



ask()
