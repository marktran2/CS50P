math = input("Expression: ")
num1, operation, num2 = math.split(sep = None, maxsplit=2)

num1 = float(num1)
num2 = float(num2)

if operation == "+":
        print(num1 + num2)
elif operation == "-":
        print(num1 - num2)
elif operation == "*":
        print(num1 * num2)
elif operation == "/":
        print(num1 / num2)


