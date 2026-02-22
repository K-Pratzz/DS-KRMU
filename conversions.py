# -----------------------------
# Step 1: Operator precedence
# -----------------------------
# Higher number = higher priority
precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}

def is_operator(ch):
    return ch in precedence


# =====================================================
# INFIX → POSTFIX
# Example Dry Run:  A+B*C
#
# Symbol | Stack | Output
# -------------------------
# A      |       | A
# +      | +     | A
# B      | +     | AB
# *      | + *   | AB
# C      | + *   | ABC
# END    | +     | ABC*
# END    |       | ABC*+
#
# Result = ABC*+
# =====================================================
def infix_to_postfix(expression):

    stack = []
    output = ""

    for ch in expression:

        # operand goes directly to output
        if ch.isalnum():
            output += ch

        # operator handling
        elif is_operator(ch):

            # pop higher/equal precedence operators
            while (len(stack) > 0 and
                   precedence[stack[-1]] >= precedence[ch]):

                output += stack.pop()

            stack.append(ch)

    # pop remaining operators
    while len(stack) > 0:
        output += stack.pop()

    return output


# =====================================================
# INFIX → PREFIX
#
# Steps:
# 1. Reverse expression
#       A+B*C → C*B+A
#
# 2. Convert to postfix
#       C*B+A → CB*A+
#
# 3. Reverse result
#       CB*A+ → +A*BC
#
# Result = +A*BC
# =====================================================
def infix_to_prefix(expression):

    expression = expression[::-1]
    postfix = infix_to_postfix(expression)
    prefix = postfix[::-1]

    return prefix


# =====================================================
# POSTFIX → INFIX
# Example: ABC*+
#
# Symbol | Stack
# -------------------------
# A      | A
# B      | A B
# C      | A B C
# *      | A (B*C)
# +      | (A+(B*C))
#
# Result = (A+(B*C))
# =====================================================
def postfix_to_infix(expression):

    stack = []

    for ch in expression:

        if ch.isalnum():
            stack.append(ch)

        else:
            op2 = stack.pop()
            op1 = stack.pop()

            new_expr = "(" + op1 + ch + op2 + ")"
            stack.append(new_expr)

    return stack.pop()


# =====================================================
# POSTFIX → PREFIX
# Example: ABC*+
#
# Symbol | Stack
# -------------------------
# A      | A
# B      | A B
# C      | A B C
# *      | A *BC
# +      | +A*BC
#
# Result = +A*BC
# =====================================================
def postfix_to_prefix(expression):

    stack = []

    for ch in expression:

        if ch.isalnum():
            stack.append(ch)

        else:
            op2 = stack.pop()
            op1 = stack.pop()

            new_expr = ch + op1 + op2
            stack.append(new_expr)

    return stack.pop()


# =====================================================
# PREFIX → INFIX
# Example: +A*BC
#
# Scan RIGHT → LEFT
#
# Symbol | Stack
# -------------------------
# C      | C
# B      | C B
# *      | (B*C)
# A      | (B*C) A
# +      | (A+(B*C))
#
# Result = (A+(B*C))
# =====================================================
def prefix_to_infix(expression):

    stack = []

    for ch in reversed(expression):

        if ch.isalnum():
            stack.append(ch)

        else:
            op1 = stack.pop()
            op2 = stack.pop()

            new_expr = "(" + op1 + ch + op2 + ")"
            stack.append(new_expr)

    return stack.pop()


# =====================================================
# PREFIX → POSTFIX
# Example: +A*BC
#
# Scan RIGHT → LEFT
#
# Symbol | Stack
# -------------------------
# C      | C
# B      | C B
# *      | BC*
# A      | BC* A
# +      | ABC*+
#
# Result = ABC*+
# =====================================================
def prefix_to_postfix(expression):

    stack = []

    for ch in reversed(expression):

        if ch.isalnum():
            stack.append(ch)

        else:
            op1 = stack.pop()
            op2 = stack.pop()

            new_expr = op1 + op2 + ch
            stack.append(new_expr)

    return stack.pop()


# -----------------------------
# MAIN PROGRAM
# -----------------------------
print("\nChoose Conversion:")
print("1. Infix → Postfix")
print("2. Infix → Prefix")
print("3. Postfix → Infix")
print("4. Postfix → Prefix")
print("5. Prefix → Infix")
print("6. Prefix → Postfix")

choice = int(input("Enter choice: "))
expr = input("Enter expression (no brackets): ")

if choice == 1:
    print("Result:", infix_to_postfix(expr))

elif choice == 2:
    print("Result:", infix_to_prefix(expr))

elif choice == 3:
    print("Result:", postfix_to_infix(expr))

elif choice == 4:
    print("Result:", postfix_to_prefix(expr))

elif choice == 5:
    print("Result:", prefix_to_infix(expr))

elif choice == 6:
    print("Result:", prefix_to_postfix(expr))