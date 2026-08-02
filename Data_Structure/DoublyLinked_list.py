# Node Class
class Node:
    def __init__(self, page):
        self.page = page
        self.prev = None
        self.next = None

# Doubly Linked List
class BrowserHistory:
    def __init__(self):
        self.head = None

    # Insert at Tail
    def visit(self, page):
        new_node = Node(page)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    # Delete a Page
    def delete(self, page):
        temp = self.head

        while temp:
            if temp.page == page:

                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next

                if temp.next:
                    temp.next.prev = temp.prev

                print("Page Deleted Successfully!")
                return

            temp = temp.next

        print("Page Not Found!")

    # Forward Traversal
    def forward(self):
        temp = self.head
        print("\nForward History:")
        while temp:
            print(temp.page, end=" -> ")
            last = temp
            temp = temp.next
        print("END")

    # Backward Traversal
    def backward(self):
        temp = self.head

        if temp is None:
            return

        while temp.next:
            temp = temp.next

        print("\nBackward History:")
        while temp:
            print(temp.page, end=" -> ")
            temp = temp.prev
        print("START")


history = BrowserHistory()

while True:
    print("\n1. Visit Page")
    print("2. Delete Page")
    print("3. Forward History")
    print("4. Backward History")
    print("5. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        page = input("Enter Website: ")
        history.visit(page)

    elif choice == 2:
        page = input("Enter Website to Delete: ")
        history.delete(page)

    elif choice == 3:
        history.forward()

    elif choice == 4:
        history.backward()

    elif choice == 5:
        print("Program Ended")
        break

    else:
        print("Invalid Choice!")