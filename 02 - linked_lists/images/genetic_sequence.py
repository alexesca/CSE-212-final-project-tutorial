class LinkedList:
    """
    Implement the LinkedList data structure.  The Node class below is an
    inner class.  An inner class means that its real name is related to
    the outer class.  To create a Node object, we will need to
    specify LinkedList.Node
    """

    class Node:
        """
        Each node of the linked list will have data and links to the
        previous and next node.
        """

        def __init__(self, data):
            """
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None
        self.tail = None

    def insert_head(self, value):
        """
        Insert a new node at the front (i.e. the head) of the
        linked list.
        """
        # Create the new node
        new_node = LinkedList.Node(value)

        # If the list is empty, then point both head and tail
        # to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then only self.head will be
        # affected.
        else:
            new_node.next = self.head # Connect new node to the previous head
            self.head.prev = new_node # Connect the previous head to the new node
            self.head = new_node      # Update the head to point to the new node

    ###################
    # Start Problem 1 #
    ###################
    def insert_tail(self, value):
        """
        Insert a new node at the back (i.e. the tail) of the
        linked list.
        """
        # Create the new node
        new_node = LinkedList.Node(value)

        # If the list is empty, then point both head and tail
        # to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then only self.tail will be
        # affected.
        else:
            new_node.prev = self.tail  # Connect new node to the previous tail
            self.tail.next = new_node  # Connect the previous tail to the new node
            self.tail = new_node       # Update the tail to point to the new node

    #################
    # End Problem 1 #
    #################

    def remove_head(self):
        """
        Remove the first node (i.e. the head) of the linked list.
        """
        # If the list has only one item in it, then set head and tail
        # to None resulting in an empty list.  This condition will also
        # cover an empty list.  Its okay to set to None again.
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # If the list has more than one item in it, then only self.head
        # will be affected.
        elif self.head is not None:
            self.head.next.prev = None  # Disconnect the second node from the first node
            self.head = self.head.next  # Update the head to point to the second node

    ###################
    # Start Problem 2 #
    ###################
    def remove_tail(self):
        """
        Remove the last node (i.e. the tail) of the linked list.
        """
        # If the list has only one item in it, then set head and tail
        # to None resulting in an empty list.  This condition will also
        # cover an empty list.  Its okay to set to None again.
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # If the list has more than one item in it, then only self.tail
        # will be affected.
        elif self.tail is not None:
            self.tail.prev.next = None  # Disconnect the second to last node from the last node
            self.tail = self.tail.prev  # Update the tail to point to the second to last node

    #################
    # End Problem 2 #
    #################

    def insert_after(self, value, new_value):
        """
        Insert 'new_value' after the first occurance of 'value' in
        the linked list.
        """
        # Search for the node that matches 'value' by starting at the
        # head of the list.
        curr = self.head
        while curr is not None:
            if curr.data == value:
                # If the location of 'value' is at the end of the list,
                # then we can call insert_tail to add 'new_value'
                if curr == self.tail:
                    self.insert_tail(new_value)
                # For any other location of 'value', need to create a
                # new node and reconenct the links to insert.
                else:
                    new_node = LinkedList.Node(new_value)
                    new_node.prev = curr       # Connect new node to the node containing 'value'
                    new_node.next = curr.next  # Connect new node to the node after 'value'
                    curr.next.prev = new_node  # Connect node after 'value' to the new node
                    curr.next = new_node       # Connect the node containing 'value' to the new node
                return # We can exit the function after we insert
            curr = curr.next # Go to the next node to search for 'value'

    ###################
    # Start Problem 3 #
    ###################
    def remove(self, value):
        """
        Remove the first node that contains 'value'.
        """
        # Search for the node that matches 'value' by starting at the
        # head of the list.
        curr = self.head
        while curr is not None:
            if curr.data == value:
                # If the location of 'value' is at the end of the list,
                # then we can call remove_tail to disconnect node
                if curr == self.tail:
                    self.remove_tail()
                # If the location of 'value' is at the start of the list,
                # then we can call remove_head to disconnect node
                elif curr == self.head:
                    self.remove_head()
                # For any other location of 'value', need to disconnect
                # the current node, and connect the prev node to the next node
                # and the other way around
                else:
                    prev_node = curr.prev
                    next_node = curr.next
                    prev_node.next = next_node  # Connect prev node to the node after current
                    next_node.prev = prev_node       # Connect next node to the node before current
                return # We can exit the function after we remove
            curr = curr.next # Go to the next node

    #################
    # End Problem 3 #
    #################

    ###################
    # Start Problem 4 #
    ###################
    def replace(self, old_value, new_value):
        """
        Searrch for all instances of 'old_value' and replace the value
        to 'new_value'.
        """
        # Search for the node that matches 'value' by starting at the
        # head of the list.
        curr = self.head
        while curr is not None:
            if curr.data == old_value:
                curr.data = new_value
            curr = curr.next  # Go to the next node to search for 'value'


    #################
    # End Problem 4 #
    #################

    def __iter__(self):
        """
        Iterate foward through the Linked List
        """
        curr = self.head  # Start at the begining since this is a forward iteration.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.next # Go forward in the linked list

    ###################
    # Start Problem 5 #
    ###################
    def __reversed__(self):
        """
        Iterate backward through the Linked List
        """
        curr = self.tail  # Start at the begining since this is a forward iteration.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.prev # Go forward in the linked list

    #################
    # End Problem 5 #
    #################

    def __str__(self):
        """
        Return a string representation of the linked list.
        """
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output

def genetic_sequence_from_string():
    gen_sequence =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    gen_sequence_linked_list = LinkedList()
    for char in gen_sequence:
        gen_sequence_linked_list.insert_tail(char)
    print(gen_sequence_linked_list)
    return gen_sequence_linked_list


def copy_genetic_sequence(original_linked_list):
    new_linked_list = LinkedList()
    current_node = original_linked_list.head
    while current_node is not None:
        new_linked_list.insert_tail(current_node.data)
        current_node = current_node.next
    print("Original sequence:", original_linked_list)
    print("New sequence     :", new_linked_list)

def create_sub_linked_lists(linked_lists, marker):
    new_linked_list = LinkedList()
    current_node = linked_lists.head
    while current_node is not None:
        if current_node.data is not marker:
            new_linked_list.insert_tail(current_node.data)
        else:
            print(new_linked_list)
            new_linked_list = LinkedList()
        current_node = current_node.next




original_gen_sequence = genetic_sequence_from_string()
print()
copy_genetic_sequence(original_gen_sequence)
print()
print("Original Sequence")
original_gen_sequence = genetic_sequence_from_string()
print()
print("Sub-sequence")
create_sub_linked_lists(original_gen_sequence, "L")


