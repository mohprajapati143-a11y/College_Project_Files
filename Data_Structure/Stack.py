#Implementing Operation of Stack in Array

stack = []

while True:
    print("\n1.Push 2.Pop 3.Peek 4.Display 5.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        stack.append(input("Enter element: "))

    elif ch == 2:
        if stack:
            print("Popped:", stack.pop())
        else:
            print("Stack Empty")

    elif ch == 3:
        if stack:
            print("Top:", stack[-1])
        else:
            print("Stack Empty")

    elif ch == 4:
        print("Stack:", stack)

    elif ch == 5:
        break