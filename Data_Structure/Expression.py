# Delimiter Checking
exp = input("Enter expression: ")

stack = []

for ch in exp:
    if ch == "(":
        stack.append(ch)
    elif ch == ")":
        if stack:
            stack.pop()
        else:
            print("Not Balanced")
            break
else:
    if len(stack) == 0:
        print("Balanced")
    else:
        print("Not Balanced")