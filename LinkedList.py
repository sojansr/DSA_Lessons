from Node import Node

#Linked List: Constructor creates a new node with the value and sets the head and tail to the same node. Sets LL length to 1.
#Always check 3 scenarios: 
#1. Linked list has multiple nodes
#2. Linked list has only one node
#3. Linked list has no nodes
class LinkedList:
    #region Dunder methods
    def __init__(self, value):
        created_node = Node(value)
        self.head = created_node
        self.tail = created_node
        self.length = 1
    #endregion

    #region Linked List Operations
    def append(self, value):
        new_tail_node = Node(value)
        if self.head is not None:
            self.tail.next = new_tail_node
            self.tail = new_tail_node
        else:
            self.head = new_tail_node
            self.tail = new_tail_node
        self.length+=1
        return True

    def prepend(self,value):
        new_head_node = Node(value)
        if self.head is not None:
            new_head_node.next = self.head
            self.head = new_head_node
        else:
            self.head = new_head_node
            self.tail = new_head_node
        self.length+=1
        return True

    def pop(self):
        if self.length == 0:
            return None
        current_node = self.head
        prev_node = self.head
        while current_node.next:
            prev_node = current_node
            current_node = current_node.next
        self.tail = prev_node
        self.tail.next = None
        self.length -=1
        if self.length == 0:
            self.head = None
            self.tail = None
        return current_node    

    def pop_at_head(self):
        if self.length == 0:
            return None
        current_head_node = self.head
        new_head_node = self.head.next
        current_head_node.next = None
        self.head = new_head_node
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return current_head_node

    #endregion

    #region Search Methods
    def search_by_value(self, value):
        if self.head is None:
            return None
        temp_node = self.head
        while temp_node is not None:
            if temp_node.value == value:
                return temp_node
            temp_node = temp_node.next
        return None

    def search_by_index(self, search_index):
        if search_index > self.length:
            raise Exception("Index out of range.")
        found_index = 0
        current_node = self.head
        while current_node is not None:
            if found_index == search_index:
                return current_node
            
            found_index+=1
            current_node = current_node.next
    #endregion
    
    #region Print Methods
    def print_linked_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next
    #endregion