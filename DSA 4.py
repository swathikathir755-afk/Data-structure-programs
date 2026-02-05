# Priority Queue ADT using list
priority_queue = []
def insert():
 element = raw_input("Enter element: ")
 priority = input("Enter priority (lower number = higher priority): ")
 priority_queue.append((priority, element))
 priority_queue.sort()
 print "Element inserted successfully."
def delete():
 if len(priority_queue) == 0:
 print "Priority Queue is empty."
 else:
 item = priority_queue.pop(0)
 print "Deleted element is:", item[1]
def display():
 if len(priority_queue) == 0:
 print "Priority Queue is empty."
 else:
 print "Priority Queue elements are:"
 for item in priority_queue:
 print "Element:", item[1], " Priority:", item[0]
while True:
 print "\n--- Priority Queue ADT ---"
 print "1. Insert"
 print "2. Delete"
 print "3. Display"
 print "4. Exit"
 choice = input("Enter your choice: ")
 if choice == 1:
 insert()
 elif choice == 2:
 delete()
 elif choice == 3:
 display()
 elif choice == 4:
 print "Exiting program."
 break
 else:
 print "Invalid choice. Try again."
