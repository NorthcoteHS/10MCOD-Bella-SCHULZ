
    
# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

def print('Select operation.' )
def print('1.add')
def print('2.subtract')
def print('3.multiply')
def print('4.divide')

# Take input from user
choice = input('Enter choice(1/2/3/4:')

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

if choice == '1':
    print(num1,'+',num2,'=', add(num1,num2))

elif choice == '2':
    print(num1,'-',num2,'=', subtract(num1,num2))

elif choice == '3':
    print(num1,'*',num2,'=', multiply(num1,num2))

elif choice == '4':
    print(num1,'/',num2,'=', divide(num1,num2))
else:
    print('Invalid input')

#!/usr/bin/python

import os
import time

try:
    while True:
            print("wait for 5 sec...")
            time.sleep(5)
            print("Restarting...")
            os.execv('/home/pi/myPiConfig/Test/restartMySelf.py',  [''])
except KeyboardInterrupt:
    print(" Quit")
except Exception as e:
    print(" Quit with error " + str(e))


