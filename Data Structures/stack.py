""""
Author : Md. Asif Parvez Sarker
Home : Bangladesh
Phone : 01744861779
"""

#This is Stack Class
class Stack:
    def __init__(self):
        self.items=[]

    #this function insert value in top of the stack
    def push(self,item):
        self.items.append(item)

    #This function remove value from top of the stack
    def pop(self):
        return self.items.pop()

    #this Function return size of the stack
    def size(self):
        return len(self.items)

    #This function return stack is empty or not
    def isEmpty(self):
        return self.items==[]

    #This function return top value of the stack if stack is not empty
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    #This function return full stack
    def getStack(self):
        return  self.items

#Stack object is created and name of the object is s
s = Stack()

#All operation of stack
s.push(1)
s.push(10)
print(s.getStack())
s.pop()
print(s.getStack())
s.push(20)
s.push(30)
print(s.getStack())
print(s.isEmpty())
print(s.peek())
print(s.size())


