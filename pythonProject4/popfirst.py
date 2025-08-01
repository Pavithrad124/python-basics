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

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

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

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):  # 1 2 3
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    def mid_val(self):
        if(self.length==0):
            return None
        temp=self.head
        mid=self.length//2
        for _ in range(mid):
            temp=temp.next
        return temp.value
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
print("===========================")
print("Prepend")
my_linked_list.prepend(100)
my_linked_list.print_list()
print("===========================")
print("Pop")
my_linked_list.pop()
my_linked_list.print_list()
print("===========================")
print("mid value",my_linked_list.mid_val())
print("sum",my_linked_list.sum_of_elements())


