import view
import model


def run():
    while True:
            num1, operation, num2 = view.get_user_input()
            result = model.calculate(num1, num2, operation)
            radius = view.get_user_input()
            result_circle = model.calculate_square_circle(radius)
            length, width = view.get_user_input()
            result_rectangle = model.calculate_square_rectangle(length, width)
            view.display_result(result)
            view.display_result_circle(result_circle)
            view.display_result_rectangle(result_rectangle)
