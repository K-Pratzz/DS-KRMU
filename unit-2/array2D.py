def matrix_operations(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # 1. Row Sums
    for i in range(rows):
        print(f"Sum of Row {i}: {sum(matrix[i])}")

    # 2. Column Sums
    for j in range(cols):
        col_sum = sum(matrix[i][j] for i in range(rows))
        print(f"Sum of Col {j}: {col_sum}")

    # 3. Search for a value
    target = 30
    found = False
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == target:
                print(f"Value {target} found at ({r}, {c})")
                found = True
    
    # 4. Transpose (Conceptual Output)
    transpose = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
    print("Transpose Matrix:")
    for row in transpose:
        print(row)

# --- Execution ---
example_matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

matrix_operations(example_matrix)