# Задание 3. Номер столбца с наименьшим произведением элементов.


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
    products = []
    for col in range(cols):
        product = 1
        for row in range(rows):
            product *= matrix[row][col]
        products.append(product)

    min_product = min(products)
    # При равных произведениях выбирается первый столбец.
    min_col = products.index(min_product)
    print(f"Номер столбца с наименьшим произведением: {min_col + 1}")
    print(f"Наименьшее произведение: {min_product}")


if __name__ == "__main__":
    main()
