def get_user_input():
    choice = input('Что вы хотите использовать: обычный калькулятор (введите 1) или калькулятор площадей (введите 2)? Ввод: ')
    if choice == '1':
        num1 = float(input('Введите первое число: '))
        num2 = float(input('Введите второе число: '))
        operation = input('Введите операцию: ')
        return num1, num2, operation
    elif choice == '2':
        figure = input('Введите фигуру: круг, прямоугольник/квадрат: ')
        if figure == 'круг':
            radius = int(input('Введите радиус круга: '))
            return radius
        elif figure == 'прямоугольник' or figure == 'квадрат':
            length = int(input('Введите длину прямоугольника/квадрата: '))
            width = int(input('Введите ширину прямоугольника/квадрата: '))
            return length, width
        else:
            print('Ты уверен, что ввёл фигуру правильно?')
        return figure
    return choice
def display_result(result):
    print(f"Результат из обычного калькулятора: {result}")
def display_result_circle(result_circle):
    print(f"Результат из калькулятора площади круга: {result_circle}")
def display_result_rectangle(result_rectangle):
    print(f"Результат из калькулятора площади прямоугольника: {result_rectangle}")
