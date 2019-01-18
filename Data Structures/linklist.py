""""
Author : Md. Asif Parvez Sarker
Home : Bangladesh
Phone : 01744861779
Topic : implementation of singly Link List using python
"""

class Node:
    # Node class
    def __init__(self,data):
        self.data=data
        self.next=None
        

class LinkList:
    # Link List Class
    def __init__(self):
        self.head=None


    def listLength(self):
        # Return the length of link list
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length
    

    def insertHead(self,newNode):
        # Insert the value in the head of link list

        temporaryNode = self.head
        self.head = newNode
        self.head.next = temporaryNode
        del temporaryNode
        

    def insertEnd(self,newNode):
        # Insert the value in the end of link list
        if self.head is None:
            self.head = newNode
        else:
            lastNode=self.head
            while(True):
                if lastNode.next is None:
                    break
                lastNode=lastNode.next
            lastNode.next=newNode
            

    def insertAt(self,newNode,position):
        # Insert the value in the specific position of link list

        if position < 0 or position >self.listLength():
            print("Invalid Position")
            return
        if position is 0:
            self.insertHead(newNode)
            return
        currentNode = self.head
        currentPosition = 0

        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1
            

    def isListEmpty(self):
        # Return link list Emplty or not
        if self.head == None:
            return True
        else:
            return False

    def deleteHead(self):
        # Delete the head node of link list
        if self.isListEmpty() is False:
            previousHead = self.head
            self.head = self.head.next
            previousHead.next = Node
        else:
            print("Linked List is empty delete failed")

    def deleteEnd(self):
        # Delete the End of link list
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next

        previousNode.next = None

    def deleteAt(self,position):
        # Delete in the specific position of link list
        if position < 0 or position>= self.listLength():
            print("Invalid position")
            return
        if self.isListEmpty() is False:
            if position is 0:
                self.deleteHead()
                return
            currentNode = self.head
            currentPosition = 0

            while True:
                if currentPosition == position:
                    previousNode.next = currentNode.next
                    currentNode.next = None
                    break

                previousNode = currentNode
                currentNode = currentNode.next
                currentPosition += 1

        else:
            print("list is empty")

    def printLinkList(self):
        
        # Print the hole link list

        if self.head is None:
            print("Empty List")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next



# Testing the link list

firstNode = Node("asif")
secondNOde = Node("parvez")
thirdNode = Node("sarker")
fourthNode = Node("Md. ")

linklist = LinkList()

linklist.insertEnd(firstNode)
linklist.insertEnd(secondNOde)
linklist.insertEnd(thirdNode)




linklist.printLinkList()

linklist.deleteAt(1)

linklist.printLinkList()








