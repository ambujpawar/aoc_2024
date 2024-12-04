import re
from utils.read_input import read_input

file_path = "data/day_4.txt"


def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    xmas_count = 0
    # Directions: right, down, diagonal down-right, diagonal down-left, 
    # left, up, diagonal up-right, diagonal up-left
    directions = [
        (0, 1),   # right
        (1, 0),   # down
        (1, 1),   # diagonal down-right
        (1, -1),  # diagonal down-left
        (0, -1),  # left
        (-1, 0),  # up
        (-1, 1),  # diagonal up-right
        (-1, -1)  # diagonal up-left
    ]
    
    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols
    
    def check_word(r, c, dr, dc):
        # Check if XMAS can be formed starting from this position
        word = "XMAS"
        for i, letter in enumerate(word):
            nr, nc = r + i*dr, c + i*dc
            if not is_valid(nr, nc) or grid[nr][nc] != letter:
                return False
        return True
    
    # Iterate through every cell as a potential starting point
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if check_word(r, c, dr, dc):
                    xmas_count += 1
    
    return xmas_count


def part1():
    data = read_input(file_path)
    grid = []
    for line in data:
        grid.append(list(line))
    sol_1 = find_xmas(grid)
    print(f"Solution to Part1: {sol_1}")


def count_cross_mas_at_pos(m, i, j):
    if m[i][j] != 'A':
        return 0
    elif i == 0 or i == len(m)-1 or j == 0 or j == len(m[0])-1:
        return 0
    elif sorted([m[i-1][j-1], m[i+1][j-1], m[i-1][j+1], m[i+1][j+1]]) != ['M', 'M', 'S', 'S']:
        return 0
    elif m[i-1][j-1] == m[i+1][j+1]:
        return 0
    else:
        return 1

def count_cross_mas(m):
    return sum(count_cross_mas_at_pos(m, i, j) for i in range(len(m)) for j in range(len(m[i])))

def part2():
    data = read_input(file_path)
    grid = []
    for line in data:
        grid.append(list(line))
    sol_2 = count_cross_mas(grid)
    print(f"Solution to Part2: {sol_2}")

part1()
part2()