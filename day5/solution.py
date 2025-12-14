from typing import List

RangeType = List[int]

def sum_ranges(ranges: list[RangeType]) -> int:
    total = 0
    for start, end in ranges:
        print(f"Range: {start} {end}")
        total += end - start + 1
    return total

def is_in_range(value: int, merged_ranges: list[RangeType]) -> bool:
    n = len(merged_ranges)
    left = 0
    right = n - 1
    while left <= right:
        m = (left + right) // 2
        if merged_ranges[m][0] <= value < merged_ranges[m][1]:
            return True
        if value < merged_ranges[m][0]:
            right = m - 1
        else:
            left = m + 1
    return False

def find_solution(ids: list[int], merged_ranges: list[RangeType]) -> int:
    ids_in_ranges = 0
    for value in ids:
        if is_in_range(value, merged_ranges):
            ids_in_ranges += 1
    return ids_in_ranges

def merge_ranges(ranges: list[RangeType]) -> list[RangeType]:
    ranges.sort(key=lambda x: x[0])
    merged = [ranges[0]]
    for range in ranges[1:]:
        if range[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], range[1])
        else:
            merged.append(range)     
    return merged

def parse_input(data: list[str]) -> tuple[list[RangeType], list[int]]:
    ranges = []
    ids = []
   
    n = len(data)
    i = 0
    while i < n:
        line = data[i]
        if line == '\n':
            i += 1
            break
        start, end = line.strip().split('-')
        ranges.append([int(start), int(end)])
        i += 1

    while i < n:
        line = data[i]
        if line.strip():
            ids.append(int(line.strip()))
        i += 1
        
    return ranges, ids

def main():
    # Read and parse input
    with open('input.txt', 'r') as file:
        data = file.readlines()
        ranges, ids = parse_input(data)

    # Merge ranges
    merged_ranges = merge_ranges(ranges)

    # solution = find_solution(ids, merged_ranges)
    solution = sum_ranges(merged_ranges)

    print("Solution:", solution)


###################################################################

if __name__ == "__main__":
    main()