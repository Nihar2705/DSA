#Queue

# 1. EnQueue
# 2. DeQueue
# 3. Display Queue
# 4. IsEmpty()
# 5. IsFull()
# 6. Delete
# 7. Peek()
    
import sys
class Queue:
    def __init__(self, size):
        self.myQueue = [] #creating stack
        self.queueSize = size # stack size defined

    def isFull(self):
        if len(self.myQueue) == size:
            return True
        else:
            return True

    def enQueue(self, value):
        if self.isFull():
            print("Queue is Full")
        else:
            self.myQueue.append(value)

    def display(self):
        print(self.myQueue)
    
    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            self.myQueue.pop(0)
        
size = int(input("Enter the size of Queue : "))
obj = Queue(size)
print("Stack is created :")
while True:
    print("1. Push Operation")
    print("2. Display Queue")
    print("3. Delete Operation")
    print("4. Peek Operation")
    print("5. Delete Queue")
    print("6. Exit")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        value = int("Enter any value you  want to enter in the queue")
        obj.enQueue(value)
    elif choice == 2:
        obj.display()
