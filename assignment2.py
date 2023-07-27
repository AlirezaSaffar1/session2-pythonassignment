print("Welcome to triangle finder!")
a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
c = int(input("Enter num3: "))
if a + b > c and a + c > b and b + c > a:
    print("that's a triangle!")
else:
    print("that's not a triangle.")
