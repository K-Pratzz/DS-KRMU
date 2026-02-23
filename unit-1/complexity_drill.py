import math

def complexity_drill(n):
    print(f"--- Analysis for n = {n} ---")

    # 1. Single Loop: O(n)
    count = 0
    for i in range(n):
        count += 1
    print(f"Single Loop: {count} operations. Label: O(n)")
    print("Justification: The loop runs exactly n times linearly.\n")

    # 2. Nested Loop: O(n^2)
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    print(f"Nested Loop: {count} operations. Label: O(n^2)")
    print("Justification: For every 1 step of i, j runs n times (n * n).\n")

    # 3. Triangular Loop: O(n^2)
    count = 0
    for i in range(n):
        for j in range(i): # j only goes up to i
            count += 1
    print(f"Triangular Loop: {count} operations. Label: O(n^2)")
    print("Justification: Sum of 1 to n is n(n+1)/2, which simplifies to O(n^2).\n")

    # 4. Halving Loop: O(log n)
    count = 0
    temp_n = n
    while temp_n > 1:
        temp_n //= 2
        count += 1
    print(f"Halving Loop: {count} operations. Label: O(log n)")
    print(f"Justification: Input is divided by 2 each step. log2({n}) ≈ {math.log2(n):.2f}.\n")

complexity_drill(10)

#questions:
#big o vs big theta
#big o means the program will run at most this time, while big theta means it will run exactly this
#  time. exactly that much operations in worst case.