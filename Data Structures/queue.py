""""
Author : Md. Asif Parvez Sarker
Home : Bangladesh
Phone : 01744861779
Topic : implementation of Queue using python
"""

class Queue:
    def __init__(self):
        self.items=[]

    def enqueue(self,item):
        """This method insert item into queue"""
        self.items.insert(0,item)

    def dequeue(self):
        """This method delete item from queue"""
        self.items.pop()

    def isEmpty(self):
        """This method return queue is empty or not"""
        return self.items==[]

    def size(self):
        """This method return size of queue"""
        return len(self.items)

    def peek(self):
        """This method return top value of queue"""
        if not self.isEmpty():
            return self.items[-1]

    def getQueue(self):
        """This method return full queue"""
        return self.items


"""queue object create and do the operation"""

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)

print(queue.getQueue())

queue.dequeue()
queue.dequeue()

print(queue.getQueue())

print(queue.size())
print(queue.isEmpty())
print(queue.peek())

print()
