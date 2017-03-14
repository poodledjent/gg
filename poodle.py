print("Welcome to our calculator!")

X = int(input("Please Input a number: "))
Y = int(input("Please Input another number: "))

op = input("Please Input operation: ")
print("g: " + str(g))

if op == "-":
    z = X-Y
else:
    if op == "=":
        z = X-Y
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
