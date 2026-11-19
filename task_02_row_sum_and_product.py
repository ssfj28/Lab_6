# Задание 2. Сумма и произведение элементов K-й строки матрицы.


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
    rows = int(input("Введите количество строк M: "))
    cols = int(input("Введите количество столбцов N: "))
    while rows <= 0 or cols <= 0:
        print("Размеры матрицы должны быть положительными.")
        rows = int(input("Введите количество строк M: "))
        cols = int(input("Введите количество столбцов N: "))

    k = int(input(f"Введите номер строки K (от 1 до {rows}): "))
    while not 1 <= k <= rows:
        k = int(input(f"K должно находиться в диапазоне от 1 до {rows}. Повторите ввод: "))

    matrix = read_matrix(rows, cols)
    selected_row = matrix[k - 1]

    total = sum(selected_row)
    product = 1
    for value in selected_row:
        product *= value

    print(f"Сумма элементов строки {k}: {total}")
    print(f"Произведение элементов строки {k}: {product}")


if __name__ == "__main__":
    main()
