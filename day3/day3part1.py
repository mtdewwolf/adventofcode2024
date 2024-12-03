import re

def solve_day3(filename):
    # Read the input file
    with open(filename, 'r') as file:
        content = file.read()
    
    # Regular expression to match valid mul(X,Y) instructions
    # This looks for 'mul(' followed by 1-3 digits, then comma, then 1-3 digits, then ')'
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
    # Find all matches
    matches = re.finditer(pattern, content)
    
    total = 0
    # Process each match
    for match in matches:
        x, y = map(int, match.groups())
        result = x * y
        total += result
    
    return total

if __name__ == "__main__":
    input_file = "day3_input.txt"
    result = solve_day3(input_file)
    print(f"The sum of all multiplication results is: {result}")
