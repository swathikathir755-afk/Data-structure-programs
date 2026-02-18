# Simple BST (AVL concept )
# Supports: Insert, Delete, Search
class Node:
 def __init__(self, key):
 self.key = key
 self.left = None
 self.right = None
# Insert node
def insert(root, key):
 if root is None:
 return Node(key)
 if key < root.key:
 root.left = insert(root.left, key)
 else:
 root.right = insert(root.right, key)
 return root
# Search node
def search(root, key):
 if root is None:
 return False
 if root.key == key:
 return True
 if key < root.key:
return search(root.left, key)
 else:
 return search(root.right, key)
# Find minimum value node (used in deletion)
def minValueNode(node):
 current = node
 while current.left:
 current = current.left
 return current
# Delete node
def delete(root, key):
 if root is None:
 return root
 if key < root.key:
 root.left = delete(root.left, key)
 elif key > root.key:
 root.right = delete(root.right, key)
 else:
 # Node with only one child or no child
 if root.left is None:
 return root.right
 elif root.right is None:
 return root.left
# Node with two children: get inorder successor
 temp = minValueNode(root.right)
 root.key = temp.key
 root.right = delete(root.right, temp.key)
 return root
# Inorder traversal (prints sorted order)
def inorder(root):
 if root:
 inorder(root.left)
 print root.key,
 inorder(root.right)
