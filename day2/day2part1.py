def is_safe_report(levels):
    if len(levels) <= 1:
        return True
    
    first_diff = levels[1] - levels[0]
    if first_diff == 0:
        return False
    
    should_increase = first_diff > 0
    
    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]
        
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        
        if should_increase and diff <= 0:
            return False
        if not should_increase and diff >= 0:
            return False
    
    return True

def process_input(input_str):
    safe_count = 0
    for line in input_str.strip().split('\n'):
        if not line.strip():
            continue
        levels = [int(x) for x in line.split()]
        if is_safe_report(levels):
            safe_count += 1
    return safe_count

with open('day2_input.txt', 'r') as f:
    input_data = f.read()

result = process_input(input_data)
print(f"Number of safe reports: {result}")
