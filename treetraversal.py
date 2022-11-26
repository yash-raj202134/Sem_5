# Lab-7: Design a class that accommodates all the Tree traversal types (Inorder, Preorder, Postorder)

class Node:
    '''represent individual node '''

    def __init__(self, data) -> None:
        self.data = data  # datamembers
        self.left = None
        self.right = None

    def linkNode(self, leftNode, rightNode):
        '''a utility function to link root node to left or right childs'''
        self.left = leftNode
        self.right = rightNode
        return

class treeTraversal(object):
    '''a class that accommodates all the Tree traversal types'''

    def preorder(self, root):
        '''to perform preorder traversal'''
        if root is not None:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
        return

    def inorder(self, root):
        '''to perform inorder traversal'''
        if root is not None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)
        return

    def postorder(self, root):
        '''to perform postorder traversal'''
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")
        return


# Driver code
# Node c
n1 = Node(3)
n2 = Node(6)
n3 = Node(4)
n4 = Node(5)
n5 = Node(2)
n6 = Node(9)
n7 = Node(8)

# Tree creation
n1.linkNode(n2, n3)
n2.linkNode(n4, n5)
n3.linkNode(n6, n7)

trav = treeTraversal()
trav.preorder(n1)
print()
trav.inorder(n1)
print()
trav.postorder(n1)
