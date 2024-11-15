#Calculator using Function

def display(output):
    print("The output is", output)

def sum(a, b):
    s = a + b
    display(s)

def sub(a, b):
    s = a - b
    display(s)

def mul(a, b):
    s = a * b
    display(s)

def div(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        s = a / b
        display(s)

def calling(op, num1, num2):
    if op == "+":
        sum(num1, num2)
    elif op == "-":
        sub(num1, num2)
    elif op == "*":
        mul(num1, num2)
    elif op == "/":
        div(num1, num2)
    else:
        print("Error: Invalid operator.")

def ask():
    num1 = int(input("Enter num1: "))
    op = input("Enter the operator (+, -, *, /): ")
    num2 = int(input("Enter num2: "))
    calling(op, num1, num2)

# Start the program
ask()
