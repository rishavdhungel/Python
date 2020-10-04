#!/usr/bin/python3

#take the user input seperated by deliminator "|"
#store the numeric in seperate file num.txt and str.txt

def main():
    user_input = input("Enter a data seperated by delimiter '|':  ")
    split_input = user_input.split(sep="|")
    for i in split_input:
        if i.strip().isnumeric():
            f = open('numeric','a+')
            f.write(i)
            f.close()
        else:
            fi = open('string','a+')
            fi.write(i)
            fi.close()
    return
main()
