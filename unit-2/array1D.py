def display_array(arr, label):
    print(f"{label}: {arr}")

def insert_element(arr, pos, value):
    n = len(arr)
    # Creating space (simulating shift)
    arr.append(None) 
    shift_count = 0
    
    # Shifting elements to the right
    for i in range(n, pos, -1):
        arr[i] = arr[i-1]
        shift_count += 1
    
    arr[pos] = value
    return shift_count

def delete_element(arr, pos):
    n = len(arr)
    shift_count = 0
    
    # Shifting elements to the left
    for i in range(pos, n - 1):
        arr[i] = arr[i+1]
        shift_count += 1
    
    arr.pop() # Remove last duplicate element
    return shift_count

# --- Execution ---
my_list = [10, 20, 30, 40, 50]
print(f"Original: {my_list}")

# 1. Insert at Start (Index 0)
shifts = insert_element(my_list, 0, 5)
print(f"After Insert at Start: {my_list} | Shifts: {shifts} (O(n))")

# 2. Delete from Middle (Index 2)
shifts = delete_element(my_list, 2)
print(f"After Delete at Middle: {my_list} | Shifts: {shifts}")