# Задание 4. Количество элементов, превышающих среднее своего столбца.


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
    counts = []
    for col in range(cols):
        column_sum = sum(matrix[row][col] for row in range(rows))
        average = column_sum / rows
        count = sum(1 for row in range(rows) if matrix[row][col] > average)
        counts.append(count)
        print(f"Столбец {col + 1}: среднее = {average}, элементов больше среднего = {count}")

    print("Количество элементов по столбцам:", *counts)


if __name__ == "__main__":
    main()
