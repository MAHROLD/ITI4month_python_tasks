import os
import time
def rightarrow(num):
    for i in range(num):
        if i==(num-1):
        #prints middle line
            #++
            print(((num*3 )-1)*" ",end="");
            print((2*num)*"*",end="");
            print((i+1)*"*")
        else:
        #prints first part be4 the line
            print(((num*3)-1)*" ",end="");
            print((2*num)*" ",end="")
            print((i+1)*"*")
            
    for j in range(num-1,0,-1):
        #prints second part
        print(((num*3)-1)*" ",end="");
        print((2*num)*" ",end="")
        print((j)*"*")
    
def leftarrow(num):
    for i in range(num):
        if i== (num-1):
        #prints middle line
            print((2*num)*"*",end="");
            print((i+1)*"*")
        else:
        #prints first part be4 the line
            
            print((num-i-1)*" ",end="")
            print((i+1)*"*")
        
    for j in range(1,num,1):
        #prints second part
        print(" ",end="")
        print((num-j)*"*")
        print((j)*" ",end="")

def uparrow(num):
    #up arrow
    for i in range(num):
        print(" "*(num*2),end="")
        for j in range(i+1,num):
            print(" ",end="")
        for j in range(i):
            print("*",end="")
        for j in range(i+1):
            print("*",end="")
        print()
    for i in range(0,num*2,1):
        print(" "*(num*2),end="")
        print(" "*(num-1),end="")
        print("*")
    
def downarrow(num):
    #down arrow
    for i in range(0,num*2,1):
        print(" "*(num*2),end="")
        print(" "*(num-1),end="")
        print("*")
    for i in range(num):
        print((num*2)*" ",end="");
        for j in range(i):
            print(" ",end="")
        for j in range(i,num-1):
            print("*",end="")
        for j in range(i,num):
            print("*",end="")
        print()
    
num = input('enter a number\n')
num=int(num)
while(1):
    os.system('cls')
    for i in range(((num*2)+1)):
        print()
    rightarrow(num)
    time.sleep(.2)
    os.system('cls')
    for i in range(num*3):
        print()
    downarrow(num)
    time.sleep(.2)
    os.system('cls')
    for i in range(((num*2)+1)):
        print()
    leftarrow(num)
    time.sleep(.2)
    os.system('cls')
    print()
    uparrow(num)
    time.sleep(.2)
