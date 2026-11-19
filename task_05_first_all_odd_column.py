# Задание 5. Первый столбец, содержащий только нечётные целые числа.


def read_matrix(rows, cols):
    matrix = []
    print(f"Введите {rows} строк целочисленной матрицы, по {cols} чисел в каждой:")
    for i in range(rows):
        while True:
            values = input(f"Строка {i + 1}: ").split()
            if len(values) != cols:
                print(f"Нужно ввести ровно {cols} целых чисел.")
                continue
            try:
                matrix.append([int(value) for value in values])
                break
            except ValueError:
                print("Ошибка: в этой задаче нужны целые числа.")
    return matrix


def main():
    rows = int(input("Введите количество строк M: "))
    cols = int(input("Введите количество столбцов N: "))
    if rows <= 0 or cols <= 0:
        print("Размеры матрицы должны быть положительными.")
        return

    matrix = read_matrix(rows, cols)
    answer = 0
    for col in range(cols):
        if all(matrix[row][col] % 2 != 0 for row in range(rows)):
            answer = col + 1  # Нумерация столбцов в условии начинается с 1.
            break

    print("Номер первого столбца, состоящего только из нечётных чисел:", answer)


if __name__ == "__main__":
    main()
