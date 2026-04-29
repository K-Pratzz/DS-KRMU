from collections import deque

# Original queue
queue = deque([31, 33, 34, 35, 38, 39])

result = deque()

# -------- STEP 1: Add ODD numbers --------
for num in queue:
    if num % 2 != 0:
        result.append(num)

# -------- STEP 2: Add EVEN numbers --------
for num in queue:
    if num % 2 == 0:
        result.append(num)

# -------- OUTPUT --------
print("Rearranged Queue:")
for i in result:
    print(i, end=" ")