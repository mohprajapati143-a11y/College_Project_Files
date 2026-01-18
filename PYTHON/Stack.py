class stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def display(self):
        print("stack:", self.items)

    def size(self):
        return len(self.items)

# Testing examples
if __name__ == "__main__":
    print("Author: MOHIT PRAJAPATI")
    stack = stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    print("pop item:", stack.pop())
    print("Top item:", stack.peek())
    stack.display()
    print("Is stack empty:", stack.is_empty())
    print("Stack size:", stack.size())
    stack.pop()
    stack.pop()
    stack.pop()
    print("Is stack empty:",stack.is_empty())
    
