# This is a python program to make calculator which will perform all the basic arithematic operations

from ast import operator


num1 = float(input("Please enter any num1 : "))
num2 = float(input("Please enter any num2 : "))
operator = input("Please enter an operator, you want to perform : ")

if operator == "+" :
    print(num1 + num2)
elif operator == "-" :
    print(num1 - num2)
elif operator == "*" :
    print(num1 * num2)
elif operator == "/" :
    print(num1 / num2)
else :
    print("Invalid operator")