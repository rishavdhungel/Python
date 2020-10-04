#!usr/bin/python3

#takes an arbitrary input 
#store the input in a txt file

def main():
    filename = input("Filename: " )
    f = open(filename,'a+')
    f.write(input("Insert the data to be stored: "))
    f.close()
    return
main()

