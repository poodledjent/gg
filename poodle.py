print("Welcome to our calculator!")

X = int(input("Input a number: "))
Y = int(input("Input another number: "))

op = input("Input operation: ")
print("g: " + str(g))

if op == "+":
    z = X+Y
else:
    if op == "-":
        z = X-Y
    else:
        if op == "*":
            z = X*Y
        else:
            if op == "/":
                z = X/Y
            else:
                print("Wrong operation")
                z = 0
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
