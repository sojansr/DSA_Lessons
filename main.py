from LinkedList import LinkedList
from Node import Node

linked_list = LinkedList(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(18)

result = linked_list.pop()
result.print_node()