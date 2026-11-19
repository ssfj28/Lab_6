# Задание 7. Замена местами столбцов с глобальными минимумом и максимумом.


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
    min_value = min(min(row) for row in matrix)
    max_value = max(max(row) for row in matrix)

    # Если значение встречается несколько раз, берётся первое по строкам и столбцам.
    min_position = next((i, j) for i in range(rows) for j in range(cols)
                        if matrix[i][j] == min_value)
    max_position = next((i, j) for i in range(rows) for j in range(cols)
                        if matrix[i][j] == max_value)

    min_col = min_position[1]
    max_col = max_position[1]
    for i in range(rows):
        matrix[i][min_col], matrix[i][max_col] = matrix[i][max_col], matrix[i][min_col]

    print(f"Столбцы {min_col + 1} и {max_col + 1} поменяны местами.")
    print("Полученная матрица:")
    for row in matrix:
        print(*row)


if __name__ == "__main__":
    main()
