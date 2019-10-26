#!/usr/bin/python
from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import csv
from prettytable import from_csv
from prettytable import PrettyTable
def menu():
    correct_password = "python123"
    correct_username = "rishav"
    name = input("Enter a Username: ")
    password = input("Enter a password: ")

    if correct_password == password and correct_username == name:
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
    else:
        print("Wrong Username or Password! \n Please try again!")
        name = input("Enter a Username: ")
        password = input("Enter a password: ")
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
    with open ("data.csv", "a") as csv_file:
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
            print("No Other %name Model Found In Database!")%name
    try_again()
def show_all():
   csvfile = open("data.csv")
   x = from_csv(csvfile)
   print(x)
   csvfile.close()
   try_again()
menu()
calculation()
