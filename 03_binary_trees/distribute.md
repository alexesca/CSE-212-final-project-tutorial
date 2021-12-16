# Distribute solution

Go to the [python file](distribute.py)

### Calling the distribute function

        from tree import BST
        
        def main():
            bt = BST()
            alphabet = {
                'A': "00",
                'B': "1",
                'C': "011",
                'D': "010",
            }
            bt.distribute(alphabet)
            for x in bt:
                print(x)
        
        if __name__ == "__main__":
            main()

Go to the [python file](tree.py)

#### Distribution implementation

        def distribute(self, alphabet):
        # Reset tree root node
        self.root = BST.Node("#")
        for symbol in alphabet:
            sequence = list(alphabet[symbol])
            self._distribute(sequence, self.root, symbol)

    def _distribute(self, sequence, node, symbol):
        """
        This function will distribute a coded alphabet
        """
        if len(sequence) == 0:
            if node.data == "1":
                node.right = BST.Node(symbol)
            else:
                node.left = BST.Node(symbol)
            return

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
