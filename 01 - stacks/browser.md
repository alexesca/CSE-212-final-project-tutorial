# Back Button Solution

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


     sites_visited_stack = Stack()
     sites_visited_stack.add("https://www.byui.edu/")
     sites_visited_stack.add("https://www.byui.edu/admissions")
     sites_visited_stack.add("https://www.byui.edu/admissions/apply")
     sites_visited_stack.add("https://www.byui.edu/admissions/apply/freshmen")
     sites_visited_stack.add("https://www.byui.edu/admissions/application-help")
     sites_visited_stack.remove()
     sites_visited_stack.remove()
     sites_visited_stack.remove()

