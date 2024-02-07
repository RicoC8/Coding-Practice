class Node:
    def __init__(self, data):
        self.data = data
        self.lpointer = -1
        self.rpointer = -1 
    
tree = [Node(-1) for i in range(11)]
root = -1


def search(item):
    global root
    itempointer = root
    while tree[itempointer].data != item and itempointer != -1:
        if item < tree[itempointer].data:
            itempointer = tree[itempointer].lpointer
        else:
             itempointer = tree[itempointer].rpointer
    return itempointer

def add(item):
    global root
    if root == -1:
        root = 0
        tree[root].data = item
    else:
        itempointer = root
 
        while itempointer != -1:  
            prev = itempointer      
            if item < tree[itempointer].data:
                itempointer = tree[itempointer].lpointer
                if itempointer == -1:

                    tree[itempointer] = Node(item)
            else:
                itempointer = tree[itempointer].rpointer
                if itempointer == -1:
                    tree[prev] = Node(item)






add(5)
add(6)
print(search(5))
print(search(6))
print(search(-1))
print("Tree")
for i in range(11):
    print(tree[i].data)