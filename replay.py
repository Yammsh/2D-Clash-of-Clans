import time 
import os
input = input("Enter the file name")
f = open(input,"r")
l = f.read()
arr = l.split("-"*10)
for i in arr:
    os.system("clear")
    print(i)
    time.sleep(0.1)
