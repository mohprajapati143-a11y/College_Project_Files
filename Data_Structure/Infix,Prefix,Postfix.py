# Prefix and Postfix Expression
# Function to define precedence of operators
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

# Function to convert infix to postfix
def infix_to_postfix(expression):
    result = ""
    stack = []

    for char in expression:
        if char.isalnum():
            result += char

        elif char == '(':
            stack.append(char)

        elif char == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                result += stack.pop()
            stack.append(char)

    while stack:
        result += stack.pop()

    return result

# Function to convert infix to prefix
def infix_to_prefix(expression):
    # Reverse the expression
    expression = expression[::-1]

    # Swap brackets
    temp = ""
    for ch in expression:
        if ch == '(':
            temp += ')'
        elif ch == ')':
            temp += '('
        else:
            temp += ch

    # Convert to postfix and reverse
    postfix = infix_to_postfix(temp)
    return postfix[::-1]

# -------- User Input --------
exp = input("Enter Infix Expression: ")

print("Infix Expression :", exp)
print("Prefix Expression:", infix_to_prefix(exp))
print("Postfix Expression:", infix_to_postfix(exp))
