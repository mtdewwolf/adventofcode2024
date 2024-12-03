import re

def solve_day3_part2(filename):
    # Read the input file
    with open(filename, 'r') as file:
        content = file.read()
    
    # Find all instructions (mul, do, and don't) with their positions
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'
    
    # Get all instructions with their positions
    instructions = []
    
    # Find all mul instructions
    for match in re.finditer(mul_pattern, content):
        x, y = map(int, match.groups())
        instructions.append(('mul', match.start(), x * y))
    
    # Find all do() instructions
    for match in re.finditer(do_pattern, content):
        instructions.append(('do', match.start(), None))
    
    # Find all don't() instructions
    for match in re.finditer(dont_pattern, content):
        instructions.append(('dont', match.start(), None))
    
    # Sort instructions by their position in the text
    instructions.sort(key=lambda x: x[1])
    
    # Process instructions in order
    total = 0
    enabled = True  # mul instructions are enabled at the start
    
    for inst_type, _, value in instructions:
        if inst_type == 'do':
            enabled = True
        elif inst_type == 'dont':
            enabled = False
        elif inst_type == 'mul' and enabled:
            total += value
    
    return total

if __name__ == "__main__":
    input_file = "day3_input.txt"
    result = solve_day3_part2(input_file)
    print(f"The sum of all enabled multiplication results is: {result}")
