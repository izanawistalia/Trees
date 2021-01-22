###############################
#    SUM OF THE LEAF NODES    #
###############################

import tree

#pass root of the tree to find the sum of its leaf nodes
def leafSum(root):
    if root is None:
        return 0
    if tree.isLeafNode(root):
        return root.getData()
    total = 0
    if root.leftChild is not None:
        total+=leafSum(root.leftChild)
    if root.rightChild is not None:
        total+=leafSum(root.rightChild)
    return total

#DRIVER FUNCTION
def main():
    bt = [9,5,6,2,3,1,10,11,25,12,1]
    root = tree.rootTree(bt)
    print('leaf sum is ',leafSum(root))

if __name__=="__main__":
    main()
