class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = -1
    
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.pointer = self.head
            self.head = new_node

    def delete(self, data):
        current_node = self.head
        prev_node = self.head
        found = False
        while found == False and current_node.pointer != -1:
            if current_node.data == data:
                found = True
            else:
                prev_node = current_node
                current_node = current_node.pointer
        prev_node.pointer = current_node.pointer

    def display(self):
        current_node = self.head
        end = False
        while end == False:
            print(current_node.data)
            if current_node.pointer == -1:
                end = True
            current_node = current_node.pointer



llist = LinkedList()
llist.add(5)
llist.add(6)
llist.add(7)
llist.delete(6)
llist.display()