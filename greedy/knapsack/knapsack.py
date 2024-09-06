def read_knapsack_file(file_name):
    items = []
    
    with open(file_name, 'r') as file:
        lines = file.readlines()
        # First line gives us the number of items and the max weight of the knapsack
        num_items, knapsack_capacity = map(int, lines[0].strip().split())
        
        # From the second line onwards, read the value and weight of each item
        for line in lines[1:]:
            value, weight = map(int, line.strip().split())
            items.append((value, weight))
    
    return num_items, knapsack_capacity, items

def greedy_knapsack(num_items, knapsack_capacity, items):
    # Sort the items by value-to-weight ratio in descending order
    items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)
    
    total_value = 0
    total_weight = 0
    selected_items = []
    
    for value, weight in items:
        if total_weight + weight <= knapsack_capacity:
            selected_items.append((value, weight))
            total_weight += weight
            total_value += value
    
    return total_value, total_weight, selected_items

def main():
    file_names = ["f1_l-d_kp_10_269.txt", "f2_l-d_kp_20_878.txt", "f3_l-d_kp_4_20.txt"]
    
    for file_name in file_names:
        # Read the file
        num_items, knapsack_capacity, items = read_knapsack_file(file_name)
        
        # Apply the greedy algorithm
        total_value, total_weight, selected_items = greedy_knapsack(num_items, knapsack_capacity, items)
        
        # Print the results
        print(f"Results for {file_name}:")
        print(f"Total value: {total_value}")
        print(f"Total weight: {total_weight}")
        print(f"Selected items: {selected_items}\n")

if __name__ == "__main__":
    main()

