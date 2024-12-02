"""Solution to day 1 of Advent of Code"""
from collections import Counter
from utils.read_input import read_input

file_path = "data/day_2.txt"


def is_safe_sequence(sequence):
    """
    Check if a sequence is safe by verifying:
    1. All levels are either increasing or decreasing
    2. Adjacent levels differ by at least 1 and at most 3
    """
    # Check if increasing
    increasing = all(sequence[i+1] - sequence[i] >= 1 and 
                     sequence[i+1] - sequence[i] <= 3 
                     for i in range(len(sequence)-1))
    
    # Check if decreasing
    decreasing = all(sequence[i] - sequence[i+1] >= 1 and 
                     sequence[i] - sequence[i+1] <= 3 
                     for i in range(len(sequence)-1))
    
    return increasing or decreasing


def part1():
    """
    Count safe reports in Part 1
    """
    data = read_input(file_path)
    data  = [list(map(int, line.split())) for line in data]
    
    sol_1 = sum(1 for report in data if is_safe_sequence(report))
    print(f"Solution to Part1: {sol_1}")


def part2():
    data = read_input(file_path)
    data  = [list(map(int, line.split())) for line in data]
    
    safe_reports = 0

    for report in data:
        # First check if report is already safe
        if is_safe_sequence(report):
            safe_reports += 1
            continue
        
        # Try removing each level
        found_safe = False
        for i in range(len(report)):
            # Create a new sequence without the i-th element
            modified_report = report[:i] + report[i+1:]
            
            # Check if modified report is safe
            if is_safe_sequence(modified_report):
                found_safe = True
                break
        
        if found_safe:
            safe_reports += 1

    print(f"Solution to Part2: {safe_reports}")

part1()
part2()