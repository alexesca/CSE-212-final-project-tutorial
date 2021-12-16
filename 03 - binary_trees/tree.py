class BST:
    """
    Implement the Binary Search Tree (BST) data structure.  The Node
    class below is an inner class.  An inner class means that its real
    name is related to the outer class.  To create a Node object, we will
    need to specify BST.Node
    """

    class Node:
        """
        Each node of the BST will have data and links to the
        left and right sub-tree.
        """

        def __init__(self, data):
            """
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """

            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def distribute(self, alphabet):
        # Resets tree root node
        self.root = BST.Node("#")
        # Traverses dictionary
        for symbol in alphabet:
            sequence = list(alphabet[symbol])
            self._distribute(sequence, self.root, symbol)

    def _distribute(self, sequence, node, symbol):
        """
        This function will distribute a coded alphabet
        """

        # If sequence is empty, insert symbol
        if len(sequence) == 0:
            if node.data == "1":
                node.right = BST.Node(symbol)
            else:
                node.left = BST.Node(symbol)
            return

        # Get current code
        current_code = sequence.pop(0)
        if current_code == "1":
            if node.right is None:
                node.right = BST.Node(current_code)
            node = node.right
        elif current_code == "0":
            if node.left is None:
                node.left = BST.Node(current_code)
            node = node.left
        self._distribute(sequence, node, symbol)

    def insert(self, data):
        """
        Insert 'data' into the BST.  If the BST
        is empty, then set the root equal to the new
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    ###################
    # Start Problem 1 #
    ###################
    def _insert(self, data, node):
        """
        This function will look for a place to insert a node
        with 'data' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        """
        if data == node.data:
            print("Duplicate!!!")
        elif data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)

    #################
    # End Problem 1 #
    #################

    def __contains__(self, data):
        """
        Checks if data is in the BST.  This function
        supports the ability to use the 'in' keyword:

        if 5 in my_bst:
            ("5 is in the bst")

        """
        return self._contains(data, self.root)  # Start at the root

    ###################
    # Start Problem 2 #
    ###################
    def _contains(self, data, node):
        """
        This funciton will search for a node that contains
        'data'.  The current sub-tree being search is
        represented by 'node'.  This function is intended
        to be called the first time by the __contains__ function.
        """
        # We found it!!!
        if data == node.data:
            return True
        elif data < node.data:
            # The data belongs on the left side.
            if node.left is not None:
                return self._contains(data, node.left)
        elif data > node.data:
            # The data belongs on the right side.
            if node.right is not None:
                return self._contains(data, node.right)
        # Default option
        return False

    #################
    # End Problem 2 #
    #################

    def __iter__(self):
        """
        Perform a forward traversal (in order traversal) starting from
	    the root of the BST.  This is called a generator function.
        This function is called when a loop	is performed:

        for value in my_bst:
            print(value)

        """
        yield from self._traverse_forward(self.root)  # Start at the root

    def _traverse_forward(self, node):
        """
        Does a forward traversal (in-order traversal) through the
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the left
        side (thus getting the smaller numbers first), then we will
        provide the data in the current node, and finally we will
        traverse on the right side (thus getting the larger numbers last).

        The use of the 'yield' will allow this function to support loops
        like:

        for value in my_bst:
            print(value)

        The keyword 'yield' will return the value for the 'for' loop to
	    use.  When the 'for' loop wants to get the next value, the code in
	    this function will start back up where the last 'yield' returned a
	    value.  The keyword 'yield from' is used when our generator function
        needs to call another function for which a `yield` will be called.
        In other words, the `yield` is delegated by the generator function
        to another function.

        This function is intended to be called the first time by
        the __iter__ function.
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)

    def __reversed__(self):
        """
        Perform a formward traversal (in order traversal) starting from
        the root of the BST.  This function is called when a the
        reversed function is called and is frequently used with a for
        loop.

        for value in reversed(my_bst):
            print(value)

        """
        yield from self._traverse_backward(self.root)  # Start at the root

    ###################
    # Start Problem 3 #
    ###################
    def _traverse_backward(self, node):
        """
        Does a backwards traversal (reverse in-order traversal) through the
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the right
        side (thus getting the larger numbers first), then we will
        provide the data in the current node, and finally we will
        traverse on the left side (thus getting the smaller numbers last).

        This function is intended to be called the first time by
        the __reversed__ function.
        """
        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)

    #################
    # End Problem 3 #
    #################

    def get_height(self):
        """
        Determine the height of the BST.  Note that an empty tree
        will have a height of 0 and a tree with one item (root) will
        have a height of 1.

        If the tree is empty, then return 0.  Otherwise, call
        _get_height on the root which will recursively determine the
        height of the tree.
        """
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)  # Start at the root

    ###################
    # Start Problem 4 #
    ###################
    def _get_height(self, node):
        """
        Determine the height of the BST.  The height of a sub-tree
        (represented by 'node') is 1 plus the height of either the
        left sub-tree or the right sub-tree (whichever one is bigger).

        This function intended to be called the first time by
        get_height.
        """
        if node.left is None and node.right is None:
            return 1
        elif node.left is not None and node.right is None:
            return 1 + self._get_height(node.left)
        elif node.right is not None and node.left is None:
            return 1 + self._get_height(node.right)
        elif node.left is not None and node.right is not None:
            return max(
                1 + self._get_height(node.left),
                1 + self._get_height(node.right)
            )

    #################
    # End Problem 4 #
    #################
