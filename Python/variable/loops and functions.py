def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Error: Invalid operator"

print(calculate(10, "+", 5))
print(calculate(10, "/", 0))


fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

command = ""

while command != "quit":
    command = input("Type 'quit' to stop: ")
