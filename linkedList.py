class Node:
    def __init__(self, data, reference=None):
        self.data = data
        self.reference = reference

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def print_linked_list(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            c_node = self.head
            while c_node is not None:
                print(c_node.data)
                c_node = c_node.reference

    def add_to_start(self, data):
        n_node = Node(data)
        n_node.reference = self.head
        self.head = n_node

# Create nodes
node1 = Node(5)
node2 = Node(11)

# Link nodes
node1.reference = node2

# Create linked list
linked_list1 = LinkedList()
linked_list1.head = node1

# Add more nodes
linked_list1.add_to_start(82)
linked_list1.add_to_start(15)

# Print linked list
linked_list1.print_linked_list()
