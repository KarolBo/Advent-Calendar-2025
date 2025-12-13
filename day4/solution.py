def check_accessibility(grid: list[list[bool]], x: int, y: int) -> bool:
    neighbors_count = 0
    w = len(grid[0])
    h = len(grid)
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            new_x = x + i
            new_y = y + j
            if new_x < 0 or new_x >= w or new_y < 0 or new_y >= h:
                continue
            if grid[new_x][new_y]:
                neighbors_count += 1
    return neighbors_count < 4

def find_solution_2(grid: list[list[bool]]) -> int:
    width = len(grid[0])
    height = len(grid)
    count = 0
    has_accessible = True
    while has_accessible:
        has_accessible = False
        for x in range(width):
            for y in range(height):
                if not grid[x][y]:
                    continue
                can_be_accessed = check_accessibility(grid, x, y)
                if can_be_accessed:
                    has_accessible = True
                    count += 1
                    grid[x][y] = False
    return count

def find_solution_1(grid: list[list[bool]]) -> int:
    width = len(grid[0])
    height = len(grid)
    count = 0
    for x in range(width):
        for y in range(height):
            if not grid[x][y]:
                continue
            can_be_accessed = check_accessibility(grid, x, y)
            if can_be_accessed:
                count += 1
    return count

def format_grid(lines: list[str]) -> list[list[bool]]:
    grid = []
    for line in lines:
        row = [char == '@' for char in line.strip()]
        grid.append(row)
    return grid

def main():
    with open("input.txt") as f:
        lines = f.readlines()
    grid = format_grid(lines)
    # solution = find_solution_1(grid)
    solution = find_solution_2(grid)
    print(f"Solution: {solution}")

#################################################################################

if __name__ == "__main__":
    main()