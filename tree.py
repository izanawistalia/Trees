############################
#    BINARY SEARCH TREE    #
############################


from queue import Queue


#pass it data to create a tree node and parent is optional
class Tree:
    def __init__(self,data,parent=None):
        # print(f'{data} added')
        self.data = data
        self.parent = parent
        self.leftChild = None
        self.rightChild = None

    def getData(self):
        return self.data

    def getLeftChild(self,):
        return self.leftChild.data

    def getRightChild(self):
        return self.rightChild.data


#for breadth first search, pass only the root node
def breadthFirstSearch(root):
    q = Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        print(node.getData())
        if node.leftChild is not None:
            q.put(node.leftChild)
        if node.rightChild is not None:
            q.put(node.rightChild)


#for depth first search, pass the root node only
def depthFirstSearch(root):
    if root is None:
        return
    print(root.getData())
    if root.leftChild is not None:
        depthFirstSearch(root.leftChild)
    if root.rightChild is not None:
        depthFirstSearch(root.rightChild)


#roots the tree at the first element of the list
def rootTree(elements):
    node = Tree(elements.pop(0))
    buildTree(node,elements)
    return node


#adds children to the parent node
def addChild(parent,child):
    if child<parent.getData():
        if parent.leftChild is None:
            parent.leftChild = Tree(child,parent)
        else:
            addChild(parent.leftChild,child)
    else:
        if parent.rightChild is None:
            parent.rightChild = Tree(child,parent)
        else:
            addChild(parent.rightChild,child)


#it build the tree, for the given parent node.
def buildTree(parent,children):
    for child in children:
        addChild(parent,child)


#returns if the given node is leaf node or not.
def isLeafNode(node):
    if node.leftChild is None and node.rightChild is None:
        return True
    return False


#DRIVER FUNCTION
def main():
    #bt = list(map(int,input().split()))
    bt = [9,5,6,2,3,1,10,11,25,12,1]
    root = rootTree(bt)
    breadthFirstSearch(root)
    depthFirstSearch(root)

#DRIVER CONDITION
if __name__=="__main__":
    main()
