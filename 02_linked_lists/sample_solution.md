# Creating sub linked list sample solution

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
