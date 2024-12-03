def read_input(filename):
    left_list = []
    right_list = []
    
    print(f"Reading from file: {filename}")
    with open(filename, 'r') as f:
        for line_num, line in enumerate(f, 1):
            try:
                left, right = line.strip().split()
                left_list.append(int(left))
                right_list.append(int(right))
            except Exception as e:
                print(f"Error on line {line_num}: {e}")
                print(f"Line content: '{line.strip()}'")
    
    print(f"Read {len(left_list)} pairs of numbers")
    if left_list:
        print(f"First pair: {left_list[0]}, {right_list[0]}")
        print(f"Last pair: {left_list[-1]}, {right_list[-1]}")
    
    return left_list, right_list

def calculate_total_distance(left_list, right_list):
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    
    total_distance = 0
    for l, r in zip(left_sorted, right_sorted):
        distance = abs(l - r)
        total_distance += distance
    
    return total_distance

def main():
    left_list, right_list = read_input('input.txt')
    result = calculate_total_distance(left_list, right_list)
    print(f"The total distance between the lists is: {result}")

if __name__ == "__main__":
    main()
