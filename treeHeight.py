#################################
#    FIND HEIGHT OF THE TREE    #
#################################


#import the tree.py file, to root a tree
import tree

#pass tree root to find its height
def treeHeight(root):
    if root is None:
        return -1
    return max(treeHeight(root.leftChild),treeHeight(root.rightChild))+1

#DRIVER FUNCTION
def main():
    bt = [9,5,6,2,3,1,10,11,25,12,1]
    root = tree.rootTree(bt)
    print('tree height is',treeHeight(root))

if __name__=="__main__":
    main()