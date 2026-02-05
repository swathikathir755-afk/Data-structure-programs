class Node:
 def __init__(self, data):
 self.data = data
 self.left = None
 self.right = None
# Insert a new node
def insert(root, data):
 if root is None:
 return Node(data)
 if data < root.data:
 root.left = insert(root.left, data)
 else:
 root.right = insert(root.right, data)
 return root
# Search a value
def search(root, key):
 if root is None:
 return False
 if root.data == key:
return True
 if key < root.data:
 return search(root.left, key)
 else:
 return search(root.right, key)
# Find smallest node (helper)
def findMin(node):
 while node.left is not None:
 node = node.left
 return node
# Delete a node
def delete(root, key):
 if root is None:
 return root
 if key < root.data:
 root.left = delete(root.left, key)
 elif key > root.data:
 root.right = delete(root.right, key)
 else:
 # Case 1 & 2: node has 0 or 1 child
 if root.left is None:
 return root.right
 if root.right is None:
 return root.left
 # Case 3: node has 2 children
temp = findMin(root.right)
 root.data = temp.data
 root.right = delete(root.right, temp.data)
 return root
# ----- MAIN PROGRAM -----
root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 70)
print "Searching 30:", search(root, 30)
print "Deleting 30..."
root = delete(root, 30)
print "Searching 30:", search(root, 30)
