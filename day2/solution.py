def is_repeated_1(number: str) -> bool:
    length = len(number)
    half_length = length // 2
    if length % 2 != 0:
        return False
    for i in range(half_length):
        if number[i] != number[i + half_length]:
            return False
    return True

def is_repeated_2(number: str) -> bool:
    length = len(number)
    is_repeated = False
    for window_size in range(1, length // 2 + 1):
        if length % window_size != 0:
            continue
        window_positions = length // window_size
        is_repeated = True
        for pos in range(window_positions-1):
            for i in range(window_size):
                i += pos * window_size
                if number[i] != number[i + window_size]:
                    is_repeated = False
                    break
            if not is_repeated:
                break
        if is_repeated:
            break
    return is_repeated

def eval_range(start: int, end: int, verbose: bool) -> int:
    id_sum = 0 
    for number in range(start, end + 1):
        str_num = str(number)
        if is_repeated_2(str_num):
            if verbose:
                print(f"Range {start} - {end} -> {number}")
            id_sum += number
    return id_sum
        
def format_ranges(num_range: str) -> tuple[int, int]:
    start, end = map(int, num_range.split('-'))
    return start, end

def find_solution(data, verbose=False) -> int:
    total_sum = 0
    for line in data:
        start, end = format_ranges(line)
        total_sum += eval_range(start, end, verbose)
    return total_sum

def main():
    with open('input.txt') as f:
        data = f.read()
    data = data.strip().split(',')
    solution = find_solution(data, True)
    print(f"The solution is: {solution}") 


#####################################################################

if __name__ == '__main__':
    main()