class Node:
    def __init__(self):
        self.data = -1
        self.lpointer = -1
        self.rpointer = -1

tree = [Node() for i in range(10)]
for i in range(len(tree)):
    tree[i].lpointer = i+1
tree[len(tree) - 1].lpointer = -1 

root = -1
itemPointer = 0
nextFreePointer = 0 # heap
NewItemPointer = 0 #memory location for storing
oldPointer = 0
leftBranch = None

def add(data):
    global leftBranch, NewItemPointer, nextFreePointer, root
    if NewItemPointer == -1:
        print("The Tree is FULL")
    else:
        itemPointer = root #to browse
        NewItemPointer = nextFreePointer # memory location to add
        nextFreePointer = tree[nextFreePointer].lpointer #updating next free location

        if itemPointer == -1:
            root = NewItemPointer
        else:
            while itemPointer  != -1:
                oldPointer = itemPointer
                if data < tree[itemPointer].data:
                    itemPointer = tree[itemPointer].lpointer
                    leftBranch = True
                else:
                    itemPointer = tree[itemPointer].rpointer
                    leftBranch = False
                if leftBranch == True:
                    tree[oldPointer].lpointer = NewItemPointer
                else:
                    tree[oldPointer].rpointer = NewItemPointer
        tree[NewItemPointer].data = data

def search(item):
    global root
    itemPointer = root
    while tree[itemPointer].data != item and itemPointer != -1:
        if item < tree[itemPointer].data:
            itemPointer = tree[itemPointer].lpointer
        else:
            itemPointer = tree[itemPointer].rpointer
    return itemPointer

def display():
    for i in range(len(tree)):
        print(tree[i].data)

#there are two types of traversal in trees
#1. breadth first traversal(BFT) At each level, read the entire level from left to right
#2. depth first traversal (DFT) 
#   Pre, In and Post are with respect to the ROOT
#   Pre : root --> left --> right
#   In : left --> root --> right
#   Post: left --> right --> root
res = []
def InOrder(root):

    if root.data == -1:
        return 
    else:
        InOrder(tree[root.lpointer])
        res.append(root)
        InOrder(tree[root.rpointer])




add(5)
add(4) 
add(6)

display()
print(search(5+1))


InOrder(tree[0])
print(res)



