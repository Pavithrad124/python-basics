class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def update(self, old_value, new_value):
        temp = self.head
        while temp is not None:
            if (temp.value == old_value):
                temp.value = new_value
                return "updated"
            temp = temp.next
        return "Value not present"

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.print_list()
print("===========================")
print(my_linked_list.update(3, 20))
my_linked_list.print_list()
print("===========================")
print('Length: ', my_linked_list.length)
