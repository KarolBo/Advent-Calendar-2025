def is_repeated(number: str) -> bool:
    length = len(number)
    half_length = length // 2
    if length % 2 != 0:
        return False
    for i in range(half_length):
        if number[i] != number[i + half_length]:
            return False
    return True

def eval_range(start: int, end: int, verbose: bool) -> int:
    id_sum = 0 
    for number in range(start, end + 1):
        str_num = str(number)
        if is_repeated(str_num):
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
    solution = find_solution(data)
    print(f"The solution is: {solution}") 


#####################################################################

if __name__ == '__main__':
    main()