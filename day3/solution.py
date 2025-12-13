def calc_joltage(arr: list[int]) -> int:
    joltage = 0
    for i, value in enumerate(arr):
        joltage += value * (10 ** (11 - i))
    return joltage

def find_joltage_2(bank: str, verbosity=False) -> int:
    n = len(bank)
    indices = [i for i in range(n-12, n)]
    last_left = -1
    for i in range(12):
        j = indices[i] - 1
        while j > last_left:
            if bank[indices[i]] <= bank[j]:
                indices[i] = j 
            j -= 1
        last_left = indices[i]
    joltage_str = ''.join([bank[idx] for idx in indices])
    joltage = int(joltage_str)
    if verbosity:
        print(bank, joltage)
    return joltage
                
def find_joltage(bank: str) -> int:
    max_digit = 0
    second_max_digit = 0
    n = len(bank)
    for i, battery in enumerate(bank):
        digit = int(battery)
        if digit > max_digit and i < n - 1:
            max_digit = digit
            second_max_digit = 0
        elif digit > second_max_digit:
            second_max_digit = digit
    joltage = 10 * max_digit + second_max_digit
    return joltage
        
def find_solution_1(bank_list: list[str]) -> int:
    sum_joltage = 0
    for bank in bank_list:
        bank = bank.strip().replace('\n', '')
        # sum_joltage += find_joltage(bank)
        sum_joltage += find_joltage_2(bank)
    return sum_joltage

def main():
    with open("input.txt") as f:
        lines = f.readlines()
    solution = find_solution_1(lines)
    print(f"Solution: {solution}")


########################################################

if __name__ == "__main__":
    main()