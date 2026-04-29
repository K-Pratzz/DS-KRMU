# Using list as stack
stack = [31, 33, 34, 35, 38, 39]

odd_stack = []
even_stack = []
result = []

# -------- STEP 1: Separate odd & even --------
while stack:
    num = stack.pop()   # pop from original stack
    
    if num % 2 != 0:
        odd_stack.append(num)
    else:
        even_stack.append(num)

# -------- STEP 2: Maintain original order --------
# Reverse odd stack back
while odd_stack:
    result.append(odd_stack.pop())

# Reverse even stack back
while even_stack:
    result.append(even_stack.pop())

# -------- OUTPUT --------
print("Result:")
for i in result:
    print(i, end=" ")