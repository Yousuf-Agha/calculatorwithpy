operation = input("What operation do you wish to do ? [add,minus,mult,div] ")
num1 =int(input("What is the first number of this operation? "))
num2 = int(input("What is the second number of this operation? "))
result = 0


if operation == "add":
       result = num1 + num2
       print("Result of it is " + str(result))

if operation == "minus":
       result = num1 - num2
       print("Result of it is " + str(result))

elif operation == "mult":
         result = num1 * num2
         print("Result of it is " + str(result))

elif operation == "div":
         result = num1/num2
         print("Result of it is " + str(result))