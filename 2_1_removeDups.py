"""
Remove Dups: Write code to remove duplicates from an unsorted linked list.

"""

class Node(object):
    def __init__(self, data):
        self.data = data 
        self.next = None 

class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        node.next = self.head 
        self.head = node 

    def printl(self):
        current = self.head
        while current:
            print current.data 
            current = current.next

    def removeDups(self):
        current = second = self.head 

        while current is not None:
            while second.next is not None:
                if second.next.data == current.data:
                    second.next = second.next.next
                else:
                    second = second.next 
            current = second = current.next  


l = LinkedList()
l.insert(15)
l.insert(14)
l.insert(13)
l.insert(12)
l.insert(12)
l.insert(12)
l.insert(13)


l.printl()
print "======="

l.removeDups()
l.printl()


