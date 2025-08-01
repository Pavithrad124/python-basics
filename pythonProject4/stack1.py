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
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


stack = Stack()
ip = "({[]})"
for x in ip:  # "([]])"
    if (x == '(' or x == '{' or x == '['):
        stack.push(x)  # ( ]
    else:  # ( ] )
        if (
                (x == '}' and stack.peek() == '{') or
                (x == ']' and stack.peek() == '[') or
                (x == ')' and stack.peek() == '(')):
            stack.pop()
        else:
            stack.push(x)

print(stack)
print(stack.is_empty())