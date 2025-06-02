import art
print(art.logo)
def add(n1, n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations={"+":add,
            "-":subtract,
            "*":multiply,
            "/":divide}
def calculator():
    num1=float(input("Type the first number:\n"))
    start=True
    while start:
        for symbols in operations:
            print(symbols)
        operator=input("Pick an operation:\n")
        num2=float(input("What is the next number:\n"))
        answer=operations[operator](num1,num2)
        print(f"{num1} {operator} {num2}={operations[operator](num1,num2)}")
        restart=input(f"To continue calculating with {answer} type 'y' or to restart the calculation type 'n'").lower()
        if restart=="y":
            num1=answer
        else:
            start=False
            print("\n"*50)
            calculator()

calculator()
