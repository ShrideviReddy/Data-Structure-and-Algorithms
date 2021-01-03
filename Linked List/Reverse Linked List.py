class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def reverse(self):
        prev = None
        current= self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    def printlinkedlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(3)
list1.push(2)
list1.push(1)
list1.printlinkedlist()
list1.reverse()
list1.printlinkedlist()
