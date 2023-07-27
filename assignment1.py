print("Welcome to calculator!")
import math
op = input("Enter your operation (+ , - , * , / , sin , cos , tan , cot , ! , sqrt):")

if op == "+" :
    num1 = float(input("enter number 1:"))
    num2 = float(input("enter number 2:"))
    result = num1 + num2

if op == "-" :
    num1 = float(input("enter number 1:"))
    num2 = float(input("enter number 2:"))
    result = num1 - num2

if op == "*" :
    num1 = float(input("enter number 1:"))
    num2 = float(input("enter number 2:"))
    result = num1 * num2

if op == "/" :
    num1 = float(input("enter number 1:"))
    num2 = float(input("enter number 2:"))
    if num2 == 0 :
        result = "Error!"
    else :
        result = num1 / num2

if op == "sin" :
    num = int(input("enter your number: "))
    result = math.sin(math.radians(num))

if op == "cos" :
    num = int(input("enter your number: "))
    result = math.cos(math.radians(num))

if op == "tan" :
    num = int(input("enter your number: "))
    if math.cos(math.radians(num)) == 0 :
        result = "Error!"
    else:
        result = math.tan(math.radians(num))

if op == "cot" :
    num = int(input("enter your number: "))
    if math.sin(math.radians(num)) == 0 :
        result = "Error!"
    else:
        result = 1/math.tan(math.radians(num))

if op == "!" :
    num = int(input("enter your number: "))
    if num < 0 :
        result = "Error!"
    else:        
        result = math.factorial(num)

if op == "sqrt" :
    num = int(input("enter your number: "))
    if num < 0 :
        result = "Error!"
    else:    
        result = math.sqrt(num)    

print(result)