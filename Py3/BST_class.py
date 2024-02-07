class Node:
    def __init__(self, data):
        self.data = data
        self.left = -1
        self.right = -1

class Tree:
    def __init__(self):
        self.root = None
    
    def add(self, data):
        current_node = self.root
        added = False
        if current_node == None:
            self.root = Node(data)
        else:
            while added == False:
                if data < current_node.data:
                    if current_node.left == -1:
                        current_node.left = Node(data)
                        added = True
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right == -1:
                        current_node.right = Node(data)
                        added = True
                    current_node = current_node.right
                    
myTree = Tree()
myTree.add(5)
myTree.add(7)

