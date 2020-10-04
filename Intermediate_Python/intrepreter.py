#!/usr/bin/python3

#script which takes input(arbitrary length)
#seperated by delimiter and identifies them 
#on basis of number and strings and stores them seperately

#delimiter: |

def main():
    num_token = []
    str_token = []
    user_input = input("Insert delimited data:")
    split_input = user_input.split(sep="|")
    for i in split_input:
        if i.strip().isnumeric():
            num_token.append(i)
        else:
            str_token.append(i)
    print("Numerical Inputs: {}\n String Input: {}".format(len(num_token),len(str_token)))
    return
main()
