class Node:
    def __init__(self, data):
        self.data = data
        self.left = -1
        self.right = -1
    
class Tree:
    def __init__(self):
        self.root = -1 

    def add(self, item):
        if self.root == -1:
            self.root = Node(item)
        else:
            current_node = self.root
            added = False
            while not added:
                if item < current_node.data:
                    if current_node.left == -1:
                        current_node.left = Node(5)
                    else:
                        current_node = current_node.left
                    added = True
                else:
                    if current_node.right == -1:
                        current_node.right = Node(5)
                    else:
                        current_node = current_node.right
                    added = True
                    
myTree = Tree()
myTree.add(5)
myTree.add(6)
print(myTree.root.data)