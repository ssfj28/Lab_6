# Задание 10. Суммы диагоналей квадратной матрицы, параллельных главной.


def parse_number(value):
    try:
        return int(value)
    except ValueError:
        return float(value)


def read_matrix(size):
    matrix = []
    print(f"Введите {size} строк квадратной матрицы, по {size} чисел в каждой:")
    for i in range(size):
        while True:
            values = input(f"Строка {i + 1}: ").split()
            if len(values) != size:
                print(f"Нужно ввести ровно {size} чисел.")
                continue
            try:
                matrix.append([parse_number(value) for value in values])
                break
            except ValueError:
                print("Ошибка: вводите только числа.")
    return matrix


def main():
    size = int(input("Введите порядок квадратной матрицы M: "))
    if size <= 0:
        print("Порядок матрицы должен быть положительным.")
        return

    matrix = read_matrix(size)
    print("Суммы диагоналей, параллельных главной диагонали:")

    # Сначала диагональ из правого верхнего угла (один элемент),
    # затем диагонали увеличивающейся длины, главная и далее убывающей.
    for offset in range(size - 1, -size, -1):
        diagonal = [matrix[row][col]
                    for row in range(size)
                    for col in range(size)
                    if col - row == offset]
        print(f"Смещение {offset}: сумма = {sum(diagonal)}")


if __name__ == "__main__":
    main()
