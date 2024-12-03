import re
from utils.read_input import read_input

file_path = "data/day_3.txt"

def find_mul_patterns(input_string):
    pattern = r'mul\((\d+),(\d+)\)'
    return re.findall(pattern, input_string)

def part1():
    data = read_input(file_path)
    occurences = find_mul_patterns(data[0])
    mult_results = [int(x) * int(y) for x, y in occurences]
    sol_1 = sum(mult_results)
    print(f"Solution to Part1: {sol_1}")


def part2():
    data = read_input(file_path)
    mul_enabled = True
    
    results = []
    
    # Regex to match different instructions
    pattern = r'(mul\((\d+),(\d+)\)|do\(\)|don\'t\(\))'
    
    # Find all matches
    matches = re.findall(pattern, data[0])
    for match in matches:
        full_match = match[0]
        
        # Check for do() or don't() instructions
        if full_match == 'do()':
            mul_enabled = True
        elif full_match == 'don\'t()':
            mul_enabled = False
        
        # Check for mul() instruction
        elif full_match.startswith('mul('):
            if mul_enabled:
                # Extract numbers and multiply
                num1 = int(match[1])
                num2 = int(match[2])
                results.append(num1 * num2)
    
    # Return sum of results
    sol_2 = sum(results)
    print(f"Solution to Part2: {sol_2}")

part1()
part2()