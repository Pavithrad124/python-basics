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
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail = new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
            self.length+=1
my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(3)
print('Head value:', my_linked_list.head.value)
print('Head next:', my_linked_list.head.next)
print('Tail value:', my_linked_list.tail.value)
print('Tail next:', my_linked_list.tail.next)
print('Length:', my_linked_list.length)