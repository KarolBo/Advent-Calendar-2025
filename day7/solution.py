
def add_beams(beam1, beam2):
    return str(int(beam1) + int(beam2))

def is_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def continue_beam(manifold, i, j, current_beam, split=False):
    width = len(manifold[0])
    if split:
        if i > 0:
            manifold[j][i-1] = current_beam if manifold[j][i-1] == '.' else add_beams(manifold[j][i-1], current_beam)
        if j < width:
            manifold[j][i+1] = current_beam if manifold[j][i+1] == '.' else add_beams(manifold[j][i+1], current_beam)
    else:
        manifold[j][i] = current_beam if manifold[j][i] == '.' else add_beams(manifold[j][i], current_beam)


def format_input(data):
    data[0] = data[0].replace('S', '1')
    manifold = []
    for line in data:
        manifold.append(list(line.replace('\n', '')))
    return manifold

def solution(manifold):
    height = len(manifold)
    width = len(manifold[0])
    count_split = 0
    for j in range(1, height):
        for i in range(width):
            current_beam = manifold[j-1][i]
            if is_number(current_beam):
                split=manifold[j][i] == '^'
                if split:
                    count_split += 1
                continue_beam(manifold, i, j, current_beam, split)
    return count_split

def main():
    with open("input.txt") as f:
        data = f.readlines()
    manifold = format_input(data)
    result_1 = solution(manifold)
    result_2 = sum([int(cell) for cell in manifold[-1] if is_number(cell)])
    print('Result:', result_2)


if __name__ == "__main__":
    main()