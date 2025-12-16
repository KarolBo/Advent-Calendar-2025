def list_operation(values: list[int], operator: str) -> int:
    if operator == '+':
        return sum(values)
    if operator == '*':
        result = 1
        for v in values:
            result *= v
        return result
    raise ValueError(f"Unknown operator: {operator}")

def parse_input_2(data: list[str]) -> tuple[list[list[int]], list[str]]:
    w = len(data[0])
    n = len(data)
    value_matrix = []
    operators = w * [None]
    for x, line in enumerate(data):
        line = line.replace('\n', '')
        if x == n - 1:
            operators = list(line)
        else:
            value_matrix.append(list(line))
    for _ in range(len(operators), len(value_matrix[0])):
        operators.append(' ')
    return value_matrix, operators

def find_solution_2(data: list[str]) -> int:
    value_matrix, operators = parse_input_2(data)
    w = len(value_matrix[0])
    h = len(value_matrix)

    result = 0
    current_values = []

    for x in reversed(range(w)):
        column_value = 0
        for y in range(h):
            value = value_matrix[y][x]
            if value != ' ':
                if column_value:
                    column_value *= 10
                column_value += int(value)
        if not column_value:
            continue
        current_values.append(column_value)
        if operators[x] != ' ':
            operation_result = list_operation(current_values, operators[x])
            result += operation_result
            current_values = []

    return result

def operation(a: str, b: str, operator: str) -> int:
    if operator == '+':
        return int(a) + int(b)
    if operator == '*':
        return int(a) * int(b)
    raise ValueError(f"Unknown operator: {operator}")

def find_solution_1(data: list[str]) -> int:
    value_matrix, operators = parse_input_1(data)
    w = len(value_matrix[0])
    h = len(value_matrix)
    solutions = [int(val) for val in value_matrix[0]]
    for i in range(w):
        for j in range(1, h):
            solutions[i] = operation(solutions[i], value_matrix[j][i], operators[i])
    return sum(solutions)

def parse_input_1(data: list[str]) -> tuple[list[list[int]], list[str]]:
    value_matrix = []
    operators = []
    n = len(data)
    for x, line in enumerate(data):
        if x == n - 1:
            operators = line.split()
        else:
            value_matrix.append(line.split())
    return value_matrix, operators

def main():
    with open('input.txt', 'r') as file:
        data = file.readlines()
    # solution = find_solution_1(data)
    solution = find_solution_2(data)
    print(f"Solution: {solution}")

##############################################

if __name__ == "__main__":
    main()