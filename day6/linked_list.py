class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

if __name__ == '__main__':
    object = LinkedList()
    while True:
        print('1. Add Node Linkedlist :')
        print('2. Add Node in Beginning :')
        print('3. Add Node in Between :')
        print('4. Add Node in End  :')
        print('5. Display Linked List :')
        print('6. Exit')
        ch = int(input('Enter your choice :'))
        if ch == 1:
            value = int(input('Enter value for node:'))
            object.addNode(value)
            print('Node added successfully in single linked list : ')
        elif ch == 2:
            value = int(input('Enter value for node:'))
            object.addNodeatBeg(value)
            print('Node added successfully in single linked list : ')
        elif ch == 3:
            value = int(input('Enter value for node:'))
            object.addNodeinBetween(value)
            print('Node added successfully in single linked list : ')
        elif ch == 4:
            value = int(input('Enter value for node:'))
            object.addNodeatEnd(value)
            print('Node added successfully in single linked list : ')
        elif ch == 5:
            object.display()
        elif ch == 6:
            break
        else:
            print('Invalid choice')