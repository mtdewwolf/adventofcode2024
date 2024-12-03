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

def calculate_total_distance_with_swaps(left_list, right_list):
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    min_total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))
    
    n = len(left_list)
    for i in range(n):
        for j in range(i + 1, n):
            left_copy = left_sorted.copy()
            left_copy[i], left_copy[j] = left_copy[j], left_copy[i]
            distance = sum(abs(l - r) for l, r in zip(left_copy, right_sorted))
            min_total_distance = min(min_total_distance, distance)
            
            right_copy = right_sorted.copy()
            right_copy[i], right_copy[j] = right_copy[j], right_copy[i]
            distance = sum(abs(l - r) for l, r in zip(left_sorted, right_copy))
            min_total_distance = min(min_total_distance, distance)
    
    return min_total_distance

def main():
    left_list, right_list = read_input('input.txt')
    result = calculate_total_distance_with_swaps(left_list, right_list)
    print(f"The minimum total distance between the lists (with possible swaps) is: {result}")

if __name__ == "__main__":
    main()
