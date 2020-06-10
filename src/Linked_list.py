# Linked List
'''
LL have 0(1) = append
LL have 0(1) = prepend
LL have 0(n) = lookup

DA(Dynamic Array) 0(n) = append
'''   

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value #data
        self.next_node = next_node #next value

    def get_value(self): #get the value from a node..value stored in self.value
        return self.value


    def get_next(self): # grab next value/node
        return self.next_node

    
    def set_next(self, new_next): # change pointers to node
        self.next_node = new_next



        
    


class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

        #add to tail. Tail takes a value
    def add_to_tail(self, value): 
        # how would i know if the linked list is empty. --- If head in none
      
        new_node = Node(value, None)
          #Check if no head
        if not self.head:
            #make new node the head and tail to new node
            self.head = new_node
            self.tail = new_node
        else:
            #if we do have a head
            self.tail.set_next(new_node)
            #set tail to new node
            self.tail = new_node

    def remove_head(self):
        #is there a head - check
        if not self.head:
            return None
        
        #check if head doesn't have a next value../ There should be an value if any
        if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None

            #return the head
            return head.get_value()

        #more than one value
        value = self.head.get_value()
            # set the head refrence to the current heads next node in the list
        self.head = self.head.get_next()
        return value
    #going through and checking eacj node
    def contains(self, value):
        if not self.head:
            return False

        #get refrence to the node we are currently looking at---update this as we traverse
        current = self.head
        #check to see if we're at a valid node

        while current:
            #return True if the current value im looking at matches out target value
            if current.get_value() == value:
                return True

            #Update out current node to the current node's next node
            current = current.get_next()
            # if we've gotten here then the target node isnt in our last
        return False


        
        
"""
A stack is a data structure
-Linear
-LIFO(last in, first out)- last item first to come out
-Like a stack of papers on your desk

"""

"""
Queues
enqueue - adding an item to the end pf the queue
dequeue  - remove the item at the beggining of the queue: typically returns the item that is removed
"""
        