# Задание 8. Замена местами левой верхней и правой нижней четвертей матрицы.


def parse_number(value):
    try:
        return int(value)
    except ValueError:
        return float(value)


def read_matrix(rows, cols):
    matrix = []
    print(f"Введите {rows} строк матрицы, по {cols} чисел в каждой:")
    for i in range(rows):
        while True:
            values = input(f"Строка {i + 1}: ").split()
            if len(values) != cols:
                print(f"Нужно ввести ровно {cols} чисел.")
                continue
            try:
                matrix.append([parse_number(value) for value in values])
                break
            except ValueError:
                print("Ошибка: вводите только числа.")
    return matrix


def main():
    rows = int(input("Введите чётное количество строк M: "))
    cols = int(input("Введите чётное количество столбцов N: "))
    if rows <= 0 or cols <= 0 or rows % 2 != 0 or cols % 2 != 0:
        print("M и N должны быть положительными чётными числами.")
        return

    matrix = read_matrix(rows, cols)
    half_rows = rows // 2
    half_cols = cols // 2

    # Обмениваем соответствующие элементы верхней левой и нижней правой четвертей.
    for i in range(half_rows):
        for j in range(half_cols):
            matrix[i][j], matrix[i + half_rows][j + half_cols] = (
                matrix[i + half_rows][j + half_cols], matrix[i][j]
            )

    print("Матрица после обмена четвертей:")
    for row in matrix:
        print(*row)


if __name__ == "__main__":
    main()
