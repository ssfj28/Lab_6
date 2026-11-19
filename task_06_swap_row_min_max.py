# Задание 6. Замена местами минимального и максимального элементов каждой строки.


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
    if rows <= 0 or cols <= 0:
        print("Размеры матрицы должны быть положительными.")
        return

    matrix = read_matrix(rows, cols)
    for row in matrix:
        min_index = row.index(min(row))  # Первое вхождение минимума.
        max_index = row.index(max(row))  # Первое вхождение максимума.
        row[min_index], row[max_index] = row[max_index], row[min_index]

    print("Матрица после замены минимума и максимума в каждой строке:")
    for row in matrix:
        print(*row)


if __name__ == "__main__":
    main()
