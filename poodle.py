print("Welcome to our calculator!")

X = int(input("Input a number, Charlie~~~~ : "))
Y = int(input("Input another number, Charlie~~~~: "))

op = input("Input operation: ")

if op == "-":
    z = X-Y
else:
    if op == "+":
        z = X+Y
    else:
        if op == "/":
            z = X/Y
        else:
            if op == "*":
                z = X*Y
            else:
                z = 0
                print("Wrong operation!!!")
                
"""
if op == "+":
    z = X+Y
if op == "-":
    z = X-Y
if op == "*":
    z = X*Y
if op == "/":
    z = X/Y
if 'z' not in locals():
    print("Wrong operation")
    z = 0
"""
                

print("Result: " + str(z))
