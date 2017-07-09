"""
Implement an algorithm to find the nth to last element of a singly linked
list.

For insance if linked list is 9->7->5->3 (the 2nd(nth) to last would be 5)

"""

class Node(object):

    def __init__(self, data):
        self.data = data 
        self.next = None 

class LinkedList(object):

    def __init__(self):
        self.head = None 

    # Method to add a new node at the beggining 
    def add_node(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printNthFromLast(self, nth):
        main_pointer = self.head
        ref_pointer = self.head 
     
        count  = 0
        if(self.head is not None):
            while(count < nth ):
                if(ref_pointer is None):
                    print "%d is greater than the no. of nodes in list" %(nth)
                    return
  
                ref_pointer = ref_pointer.next
                count += 1
 
        while(ref_pointer is not None):
            main_pointer = main_pointer.next
            ref_pointer = ref_pointer.next
 
        print "Node no. %d from last is %d " %(nth, main_pointer.data)
 
 
# Driver program to test above function
llist = LinkedList()
llist.add_node(5)
llist.add_node(7)
llist.add_node(9)

llist.printNthFromLast(2)  

# Time complexity is O(n), where n is the length of the linked list 

"""
Explanation: 
1. Do we know the length of the list? If we did, say it was 5, and we are asked 
to look for 2nd to last we could say 5(n) - 2(nth) = 3 (the third item) in the 
linked list would be the third item. Since it is pretty straigh-forward, it is 
likely that you won't know the length of the linked list. 

2. Note, this problem can be approached recursively, possibly doing it in O(n)

3. The iterative solution (above) is a another proach to pursue. We use the 
runner technique (two pointers) to implement this solution. 
    
    - Both pointers start at the head(beggining of the linked list)

    - We set up a counter (line 30)

    - We check (line 32+33) to see if the nth number is greater than length of 
    the list, if it is then that particular nth doesnt exist in the linked list

    Elaborate on 32-38 

    - If the nth number is not greater, set ref_pointer = ref_pointer.next to 
    move to the next Node in the LL, and increase counter by 1 (lines 37-38)

    - The ref_pointer is one Node ahead of the main_pointer so as long as the
    ref_pointer is NOT None (as in there is a next Node), keep moving the ref
    pointer by moving to the next, and as a ref pointer moves to next pointer so
    should the main pointer.   




"""




