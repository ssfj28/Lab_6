# Задание 1. Вывод квадратной матрицы по спирали против часовой стрелки.


def parse_number(value):
    """Преобразует строку в int, а при необходимости — в float."""
    try:
        return int(value)
    except ValueError:
        return float(value)


def read_matrix(size):
    matrix = []
    print(f"Введите {size} строк матрицы, по {size} чисел в каждой:")
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
                print("Ошибка: вводите только целые или вещественные числа.")
    return matrix


def counterclockwise_spiral(matrix):
    """Возвращает элементы по спирали: вниз, вправо, вверх, влево."""
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Левый столбец сверху вниз.
        for row in range(top, bottom + 1):
            result.append(matrix[row][left])
        left += 1

        # Нижняя строка слева направо.
        for col in range(left, right + 1):
            result.append(matrix[bottom][col])
        bottom -= 1

        # Правый столбец снизу вверх.
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][right])
            right -= 1

        # Верхняя строка справа налево.
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[top][col])
            top += 1

    return result


def main():
    while True:
        size = int(input("Введите нечётный порядок квадратной матрицы M: "))
        if size > 0 and size % 2 == 1:
            break
        print("M должно быть положительным нечётным числом.")

    matrix = read_matrix(size)
    result = counterclockwise_spiral(matrix)
    print("Элементы матрицы по спирали против часовой стрелки:")
    print(*result)


if __name__ == "__main__":
    main()
