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
            print(temp.value, end=" ")
            temp = temp.next
        print()

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    def prepend(self,value):
        new_node=Node(value)
        new_node.next = self.head
        self.head= new_node
        self.length += 1


    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True


    def update(self, old_value, new_value):
        temp = self.head
        while temp is not None:
            if (temp.value == old_value):
                temp.value = new_value
                return "updated"
            temp = temp.next
        return "Value not present"
    def sum_of_elements(self):
        temp = self.head
        sum = 0
        while temp is not None:
            sum += temp.value
            temp = temp.next
        return sum


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.print_list()
print("===========================")
my_linked_list.update(4, 20)
my_linked_list.print_list()
print("===========================")
print('Length: ', my_linked_list.length)
print("===========================")
print("Get ", my_linked_list.get(2))
print("===========================")
print("Insert ", my_linked_list.insert(1, 44))
my_linked_list.print_list()
my_linked_list.prepend(0)
my_linked_list.print_list()
print('Length: ', my_linked_list.length)
print("===========================")
print("sum:",my_linked_list.sum_of_elements())

