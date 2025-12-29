from typing import Tuple, List

PointType = Tuple[int, int]

def find_area(p1: PointType, p2: PointType):
    w = abs(p1[0] - p2[0]) + 1
    h = abs(p1[1] - p2[1]) + 1 
    return w * h 

def find_greatest_rectangle(data: List[PointType]) -> int:
    area = 0
    for p1 in data:
        for p2 in data:
            if p1 is p2:
                continue
            area = max(
                area, 
                find_area(p1, p2)
            )
    return area

def depict_data(data: List[PointType]):
    _, max_x, _, max_y = get_min_max(data)
    wall = [['.' for _ in range(max_x + 2)] for _ in range(max_y + 2)]
    for x, y in data:
        wall[y][x] = '#'
    for row in wall:
        print(''.join(row))

def get_min_max(data: List[PointType]) -> Tuple[int, int, int, int]:
    min_x = float('inf')
    max_x = float('-inf')
    min_y = float('inf')
    max_y = float('-inf')
    for x, y in data:
        if x <= min_x:
            min_x = x
        if x >= max_x:
            max_x = x
        if y <= min_y:
            min_y = y
        if y >= max_y:
            max_y = y
    return min_x, max_x, min_y, max_y
    
def parse_input(data: List[str]) -> List[PointType]:
    result = []
    for line in data:
        line = line.replace('\n', '')
        x, y = line.split(',')
        result.append((int(x), int(y)))
    return result


########################################################################

if __name__ == '__main__':
    with open('./input.txt') as f:
        input_lines = f.readlines()
    data = parse_input(input_lines)
    # depict_data(data)
    solution = find_greatest_rectangle(data)
    print(f'Solution: {solution}')