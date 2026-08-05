# ------------------ Linear Queue ------------------

queue = []

while True:
    print("\n----- Linear Queue -----")
    print("1. Add Task")
    print("2. Process Task")
    print("3. Display Tasks")
    print("4. Exit")

    try:
        ch = int(input("Enter Choice: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if ch == 1:
        task = input("Enter Task: ")
        queue.append(task)
        print("Task Added Successfully!")

    elif ch == 2:
        if queue:
            print("Task Completed:", queue.pop(0))
        else:
            print("No Tasks Available!")

    elif ch == 3:
        if queue:
            print("Pending Tasks:", queue)
        else:
            print("No Tasks Available!")

    elif ch == 4:
        print("Linear Queue Program Ended.")
        break

    else:
        print("Invalid Choice!")


# ------------------ Circular Queue ------------------

size = 5
queue = [None] * size
front = rear = -1

while True:
    print("\n----- Circular Queue -----")
    print("1. Add Task")
    print("2. Process Task")
    print("3. Display Tasks")
    print("4. Exit")

    try:
        ch = int(input("Enter Choice: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if ch == 1:
        task = input("Enter Task: ")

        if (rear + 1) % size == front:
            print("Queue Full!")

        else:
            if front == -1:
                front = rear = 0
            else:
                rear = (rear + 1) % size

            queue[rear] = task
            print("Task Added Successfully!")

    elif ch == 2:
        if front == -1:
            print("Queue Empty!")

        else:
            print("Task Completed:", queue[front])
            queue[front] = None

            if front == rear:
                front = rear = -1
            else:
                front = (front + 1) % size

    elif ch == 3:
        if front == -1:
            print("Queue Empty!")
        else:
            print("Pending Tasks:", end=" ")
            i = front
            while True:
                print(queue[i], end=" ")
                if i == rear:
                    break
                i = (i + 1) % size
            print()

    elif ch == 4:
        print("Circular Queue Program Ended.")
        break

    else:
        print("Invalid Choice!")