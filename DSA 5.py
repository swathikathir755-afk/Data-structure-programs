Python Program (BST Insert, Delete, Search)
# Binary Search Tree Operations
class Node:
 def __init__(self, data):
 self.data = data
 self.left = None
 self.right = None
def insert(root, data):
 if root is None:
 return Node(data)
 if data < root.data:
 root.left = insert(root.left, data)
 elif data > root.data:
 root.right = insert(root.right, data)
 return root
def search(root, key):
 if root is None:
 return False
 if root.data == key:
 return True
 elif key < root.data:
 return search(root.left, key)
 else:
return search(root.right, key)
def find_min(root):
 while root.left is not None:
 root = root.left
 return root
def delete(root, key):
 if root is None:
 return root
 if key < root.data:
 root.left = delete(root.left, key)
 elif key > root.data:
 root.right = delete(root.right, key)
 else:
 if root.left is None:
print root.data,
 inorder(root.right)
root = None
while True:
 print "\n--- Binary Search Tree Operations ---"
 print "1. Insert"
 print "2. Search"
 print "3. Delete"
 print "4. Display (Inorder)"
 print "5. Exit"
 choice = input("Enter your choice: ")
 if choice == 1:
 val = input("Enter value to insert: ")
 root = insert(root, val)
 print "Element inserted."
 elif choice == 2:
 val = input("Enter value to search: ")
 if search(root, val):
 print "Element found in BST."
 else:
 print "Element not found."
 elif choice == 3:
 val = input("Enter value to delete: ")
 return root.right
 elif root.right is None:
 return root.left
 temp = find_min(root.right)
 root.data = temp.data
 root.right = delete(root.right, temp.data)
 return root
def inorder(root):
 if root:
 inorder(root.left)
root = delete(root, val)
 print "Element deleted (if present)."
 elif choice == 4:
 print "BST elements (Inorder):"
 inorder(root)
 print
 elif choice == 5:
 print "Exiting program."
 break
 else:
 print "Invalid choice. Try again."
