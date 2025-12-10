from enum import Enum


class Side(Enum):
    LEFT = 'L'
    RIGHT = 'R'

class Dial:
    def __init__(self):
        self._position = 50
        self._total_positions = 100

    def turn(self, side: Side, steps: int, verbose: bool = False) -> int:
        if side == Side.LEFT:
            times_passed_zero = self._turn_left(steps)
        elif side == Side.RIGHT:
            times_passed_zero = self._turn_right(steps)
        else:
            raise ValueError(f"Unknown side: {side}")

        if verbose:
            print(side.value, steps, '->', self._position, times_passed_zero)
            
        return times_passed_zero

    @property
    def position(self) -> int:
        return self._position
    
    @property
    def times_passed_zero(self) -> int:
        return self._times_passed_zero

    def _turn_left(self, steps: int):
        times_passed_zero = steps // self._total_positions
        remaining_steps = steps % self._total_positions
        if self._position and self._position <= remaining_steps:
            times_passed_zero += 1

        self._position = (self._position - steps) % self._total_positions

        return times_passed_zero

    def _turn_right(self, steps: int):
        times_passed_zero = steps // self._total_positions
        remaining_steps = steps % self._total_positions
        if self._position and (self._total_positions - self._position) <= remaining_steps:
            times_passed_zero += 1

        self._position = (self._position + steps) % self._total_positions

        return times_passed_zero


def parse_instruction(instruction: str) -> tuple[Side, int]:
    side = Side(instruction[0])
    steps = int(instruction[1:])
    return side, steps

def get_sulution1(instructions: list[str]) -> int:
    real_password = 0
    dial = Dial()
    for instruction in instructions:
        side, steps = parse_instruction(instruction)
        dial.turn(side, steps)
        if dial.position == 0:
            real_password += 1
    return real_password

def get_solution2(instructions: list[str]) -> int:
    real_password = 0
    dial = Dial()
    for instruction in instructions:
        side, steps = parse_instruction(instruction)
        real_password += dial.turn(side, steps, verbose=True)
    return real_password

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        lines = file.readlines()

    # real__password = get_sulution1(lines)
    real_password = get_solution2(lines)
    print(f"The actual password is: {real_password}")