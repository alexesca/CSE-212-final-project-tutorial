# Warehouse Solution

    class Stack:
        def __init__(self):
            self.stack = []
    
        # Adds valid value to stack
        def add(self, value):
            if value:
                self.stack.append(value)
    
        # Removes value from stack
        def remove(self):
            if len(self.stack) > 0:
                return self.stack.pop()
    
        # Gets the newest value
        def peek(self):
            if len(self.stack) > 0:
                return self.stack[-1]
    
        # Gets the first or oldest value
        def first(self):
            if len(self.stack) > 0:
                return self.stack[0]
    
    
    inventory_stack = Stack()
    # Adds items to inventory
    inventory_stack.add("wood")
    inventory_stack.add("tiles")
    inventory_stack.add("marble")
    inventory_stack.add("quarts")
    inventory_stack.add("sandstone")
    inventory_stack.add("toilet")
    inventory_stack.add("sync")
    
    # Get up next item in inventory
    print()
    print("Recent Item:")
    print(inventory_stack.peek())
    
    # Get oldest item in inventory
    print()
    print("Oldest Item:")
    print(inventory_stack.first())
    
    # Dispatch newest item in inventory
    print()
    print("Dispatch item:")
    print(f"{inventory_stack.remove()} has been shipped.")
    

