class checkBST:
    def __init__(self, nodevalue):
        self.data =  nodevalue
        self.leftnode= None
        self.rightnode = None


def BST(root,left=None,right=None):
    if (root == None):
        return True
    if (left!= None and root.data <=left.data):
        return False
    if (right!=None and root.data>=right.data):
        return False

    return BST(root.leftnode, left,root) and BST(root.rightnode ,root, right)

if __name__ == '__main__':
    root= checkBST(10)
    root.leftnode=checkBST(6)
    root.rightnode= checkBST(15)

    if (BST(root,None,None)):
        print ("BST")
    else:
        print ("Not a BST")
