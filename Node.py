"Node: Induvidual node in a linked list. Value set by constructor. Next is set to none."
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def print_node(self):
        print("Current node value is: ", self.value)