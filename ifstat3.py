def max_num (num1, num2, num3):
    if num1>=num2 and num2>=num3:
        result = num1
        print(result)
    elif num2>=num1 and num2>=num3:
        result = num2
    else:
        result = num3
        print(result)
print(max_num(2,1,8))