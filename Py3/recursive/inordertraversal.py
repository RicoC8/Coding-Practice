class Node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None

root = Node(20)
root.left = Node(15)
root.left.left = Node(11)
root.left.right = Node(16)

path = []
def add(item):
    added = False
    current_node = root
    prev_node = root
    while not added:
        prev_node = current_node
        if item < root.data:
            current_node = current_node.left
            if current_node == None:
                prev_node.left = Node(item)
                added = True
        else:
            current_node = current_node.right
            if current_node == None:
                prev_node.left = Node(item)
                added = True
                
        
add(7)
        
def InOrder(root):
    if root == None:
        return
    InOrder(root.left)
    path.append(root)
    InOrder(root.right)

InOrder(root)
for i in path:
    print (i.data)
print(path)