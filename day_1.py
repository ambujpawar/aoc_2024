"""Solution to day 1 of Advent of Code"""
from collections import Counter
from utils.read_input import read_input

file_path = "data/day_1.txt"

def part1():
    data = read_input(file_path)
    left_list, right_list = [], []

    for x in data:
        left, right = x.split('   ')
        left_list.append(left)
        right_list.append(right)

    left_list.sort()
    right_list.sort()

    sol_1 = 0
    for i, j in zip(left_list, right_list):
        sol_1 += abs(int(i) - int(j))

    print(f"Solution to Part1: {sol_1}")

    # def part1():
    # data = read_input(file_path)
    # left_list, right_list = zip(*(x.split('   ') for x in data))
    # sol_1 = sum(abs(int(i) - int(j)) for i, j in zip(sorted(left_list), sorted(right_list)))
    # print(f"Solution to Part1: {sol_1}")


def part2():
    data = read_input(file_path)
    left_list, right_list = [], []

    for x in data:
        left, right = x.split('   ')
        left_list.append(int(left))
        right_list.append(int(right))

    right_counter = Counter(right_list)

    sol_2 = 0
    for x in left_list:
        if x in right_counter:
            sol_2 += x * right_counter[x]

    print(f"Solution to Part2: {sol_2}")
# part1()
part2()