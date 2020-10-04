#!/usr/bin/python3

#scrape the directory and file inside it and save it in a file
import os

def main():
    for item_1,item_2,item_3 in os.walk("/home/rishav/Git"):
        f = open('Filelist','a+')
        f.write("{}\n: {}\n: {}\n".format(item_1,item_2,item_3))
        f.close()
    return
main()
