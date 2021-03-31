class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Constructor
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("Null")

    def lenght(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def append(self, data):
        new_node = Node(data)

        # Linked list is empty
        if self.head is None:
            # simply its the first node in LL so it will head will point to it
            self.head = new_node
            return

        # If some node are there so go until you get Null and append there the new node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        """ Adding element to the starting"""
        # Create a new node
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        """Insert after a given node"""

        # Check if the prev_node is there in LL
        if not prev_node:
            print("Previous Node is not in the list")
            return

        # Create a new node
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, data_elem):
        """Delete the node having the data in node """

        cur_node = self.head

        # if head node is to be deleted
        if cur_node and cur_node.data == data_elem:
            self.head = cur_node.next
            # Remove the node
            cur_node = None
            return

        # If head is not data_elem
        pre_node = None
        while cur_node and cur_node.data != data_elem:
            pre_node = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        pre_node.next = cur_node.next
        cur_node.next = None

    def delete_at_pos(self, pos):

        cur_node = self.head
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        pre_node = None
        count = 1
        while cur_node and count != pos:
            pre_node = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            print("Position Not found")
            return

        pre_node.next = cur_node.next
        cur_node.next = None

    def swap_node(self, key_1, key_2):

        if key_1 == key_2:
            return

        prv_1  = None
        cur_1 = self.head

        

        pre_node = None
        # Search for key
        #while cur_node

llist = LinkedList()
llist.append('B')
llist.append("C")
llist.append("E")
llist.print_list()
llist.prepend("A")
llist.print_list()
llist.insert_after_node(llist.head.next.next, "D")
llist.print_list()
llist.delete_node("A")
llist.print_list()
llist.delete_at_pos(9)
llist.print_list()

