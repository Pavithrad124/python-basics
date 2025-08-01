class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return ("Stack is empty")
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
# Pop elements from the stack
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.peek())
print(stack)
print(stack.is_empty())
