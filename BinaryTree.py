
class Node:
    def __init__(self, data):
        self.data = data
        self.left=None
        self.right = None 

#Making the Binary Tree
node = Node(1)
node.left = Node(2)
node.right = Node(3)

#Inorder Traversal the binary tree
def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data)
    inorder(node.right)

inorder(node)

#Preorder Traversal of the binary tree
def preorder(node):
    if node is None:
        return
    print(node.data)
    preorder(node.left)
    preorder(node.right)

preorder(node)