def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "БРОСИТЬ!!!"
    elif operation == '**':
            return num1 ** num2

def calculate_square_circle(radius):
    return 3.1415926535898 * radius ** 2
def calculate_square_rectangle(length, width):
    return length * width
