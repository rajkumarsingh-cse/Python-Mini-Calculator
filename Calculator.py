#Python Mini Calculator

a = float(input("Enter your first number: "))
op = input("Enter your operator (+,-,*,/,%,**) ")
b = float(input("Enter your second number: "))
 
if op == '+':
    print(a + b)

elif op == '-':
    print(a - b)

elif op == '*':
    print(a * b)

elif op == '/':
    print(a / b)

elif op == '%':
    print(a % b)

elif op == '**':
    print(a ** b)

else:
    print("Invalid Operator")+++
