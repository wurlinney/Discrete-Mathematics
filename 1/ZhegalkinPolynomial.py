def sort_combinations(combinations):
    sorted_combinations = sorted(
        [combo for combo in combinations if combo != '1'],
        key=lambda x: (len(x), x)
    )
    if '1' in combinations:
        sorted_combinations.insert(0, '1')
    return sorted_combinations


def binary_to_combinations(binary_array):
    num_columns = len(binary_array[0]) - 1
    letters = [chr(97 + i) for i in range(num_columns)]

    result = []
    for row in binary_array:
        combination = ''.join(letters[i] for i in range(num_columns) if row[i] == 1)
        result.append(combination if combination else '1')

    return result


def zhegalkin_polynomial(table):
    values = [row[-1] for row in table]
    coefficients = []

    while values:
        coefficients.append(values[0])
        values = [values[i] ^ values[i + 1] for i in range(len(values) - 1)]

    letters = binary_to_combinations(table)

    result = [letters[i] for i, coefficient in enumerate(coefficients) if coefficient == 1]

    return '1' if result == ['1'] else '+'.join(sort_combinations(result))

n = int(input('Введите количество переменных: '))
print(f'Введите таблицу истинности (по одной строке, кажда строка состоит из {n+1} нулей или единиц.')
truth_table = []
for i in range(2**n):
    row = list(map(int, input().split()))
    truth_table.append(row)

result = zhegalkin_polynomial(truth_table)
print(result)
