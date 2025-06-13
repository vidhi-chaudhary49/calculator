def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input('Enter choice ("Add","Sub","Mul","Div"): ')

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input. Please enter numbers only.")
    exit()

if choice == 'Add':
    print("Result:", add(num1, num2))
elif choice == 'Sub':
    print("Result:", subtract(num1, num2))
elif choice == 'Mul':
    print("Result:", multiply(num1, num2))
elif choice == 'Div':
    print("Result:", divide(num1, num2))
else:
    print('Invalid choice. Please select from "Add","Sub","Mul","Div"')
