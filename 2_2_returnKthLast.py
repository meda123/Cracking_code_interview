"""
Implement an algorithm to find the lth to last element of a singly linked
list.

"""

class Node(object):

    def __init__(self, data):
        self.data = data 
        self.next = Node

class LinkedList(object):

    def __init__(self):
        self.head = None 

    def add_node(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printNthFromLast(self, n):
        main_ptr = self.head
        ref_ptr = self.head 
     
        count  = 0
        if(self.head is not None):
            while(count < n ):
                if(ref_ptr is None):
                    print "%d is greater than the no. pf \
                            nodes in list" %(n)
                    return
  
                ref_ptr = ref_ptr.next
                count += 1
 
        while(ref_ptr is not None):
            main_ptr = main_ptr.next
            ref_ptr = ref_ptr.next
 
        print "Node no. %d from last is %d " %(n, main_ptr.data)
 
 
# Driver program to test above function
llist = LinkedList()
llist.add_node(20)
llist.add_node(4)
llist.add_node(15)
llist.add_node(35)
 
llist.printNthFromLast(4)  


