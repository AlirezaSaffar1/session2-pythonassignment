print("Welcome to average program!")
name = input("please enter your first name:")
family = input("please enter your last name:")
a = float(input("please enter your math score:"))
b = float(input("please enter your sience score:"))
c = float(input("please enter your history score:"))
avg = (a+b+c)/3

if avg>=17:
    print(name, family, avg, "status: great")
elif avg<17 and avg>=12:
    print(name, family, avg, "status: noraml")
else:
    print(name, family, avg, "status: fail")