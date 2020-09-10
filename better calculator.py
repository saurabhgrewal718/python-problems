num1= float(input("Enter trh first number"))
num2 = float(input("Enter the sceond number"))
op = input("Type the operation you want to perform")

if op=="+":
    print("the sum is : "+ str(num2+num2))
elif op == "-":
    print("the difference is : " + str(num1-num2))
elif op == "*":
    print("the product is : " + str(num1*num2))
elif op== "/":
    print("the divison is : " + str(num1/num2))
else:
    print("Invalid Operation")