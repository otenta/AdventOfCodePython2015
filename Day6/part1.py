import re
from enum import Enum

TURN_ON = r"turn on (\d+),(\d+) through (\d+),(\d+)"
TURN_OFF = r"turn off (\d+),(\d+) through (\d+),(\d+)"
TOGGLE = r"toggle (\d+),(\d+) through (\d+),(\d+)"

turn_on_pattern = re.compile(TURN_ON)
turn_off_pattern = re.compile(TURN_OFF)
toggle_pattern = re.compile(TOGGLE)

grid = []

class State(Enum):
    ON = 1
    OFF = 2
    TOGGLE = 3

# x is for light turned off (for visualization 'cause I'm dumb)
# y is for light turned on
def create_initial_array():
    grid = [["x" for column in range(1000)] for row in range(1000)]
    return grid


def update_grid(passed_grid: list, new_coordinates: tuple[int, int], state: State) -> list:
    initial_place = new_coordinates[:2]
    final_place = new_coordinates[-2:]

    if state == state.ON:
        for row in range(initial_place[0], final_place[0] + 1):
            for column in range(initial_place[1], final_place[1] + 1):
                passed_grid[row][column] = "y"
    if state == state.OFF:
        for row in range(initial_place[0], final_place[0] + 1):
            for column in range(initial_place[1], final_place[1] + 1):
                passed_grid[row][column] = "x"
    if state == state.TOGGLE:
        for row in range(initial_place[0], final_place[0] + 1):
            for column in range(initial_place[1], final_place[1] + 1):
                if passed_grid[row][column] == "x":
                    passed_grid[row][column] = "y"
                else:
                    passed_grid[row][column] = "x"

    return passed_grid

def find_lights_on(final_grid: list) -> int:
    lights_on = 0
    for row in range (0, 1000):
        for column in range(0, 1000):
            if final_grid[row][column] == "y":
                lights_on += 1
    return lights_on

with open("input.txt") as file:
    initial_grid = create_initial_array()
    for i in file.readlines():
        match_turn_on = turn_on_pattern.match(i)
        match_turn_off = turn_off_pattern.match(i)
        match_toggle = toggle_pattern.match(i)

        if match_turn_on:
            coords_on = tuple(map(int, match_turn_on.groups()))
            initial_grid = update_grid(initial_grid, coords_on, state=State.ON)
        if match_turn_off:
            coords_off = tuple(map(int, match_turn_off.groups()))
            initial_grid = update_grid(initial_grid, coords_off, state=State.OFF)
        if match_toggle:
            coords_toggle = tuple(map(int, match_toggle.groups()))
            initial_grid = update_grid(initial_grid, coords_toggle, state=State.TOGGLE)
    print(find_lights_on(initial_grid))
