class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def print_queue(self):
        print(self.items)

    def peek(self):
        return self.items[0]


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.print_queue()
print(q.peek())
print(q.dequeue())
q.print_queue()
print("size is ", q.size())