# Stacks:

### Table of Contents

Welcome to this Stack tutorial. Mastering this important skill will help you advance further into your engineering
career, solve real life problems, and land amazing job opportunities.

1. Definition
2. Example
4. LIFO definition
5. Functionality
    1. Push
    2. Pop 
    3. Size
9. Coding Challenge 1
10. Coding Challenge 2
11. Performance
12. Do's and Don'ts
    1. When to use stacks
    2. When not to use stacks

### Definition

A stack is a data structure that is characterized by the order in which items are added and removed. Often called "Last
In, First Out" (LIFO), the stack can be used to accomplish various tasks and can be implemented using a Python **list**.
The insert and delete operations are often called push and pop. Remember that lists(the
underline data structure used by the stack) have index 0 and the last element of the stack is always the size of the
stack minus 1.

Stacks implement the **Last in, first out** method. The top of the stack is called the back and the bottom is called the
front. When items are added or pushed onto the stack, they are added to the back of the stack. When items are removed
from the stack, the last item that was added gets removed first. It is not common practice to remove items from the
middle or from the front of the stack. See queue and dynamic array to better solve you problem if stacks are not
appropriate.

![Stack Images](images/stack.png "Stack Image")

### Example

The use of a stack would benefit an application that needs to remember the last action taken by the user. Analyze the
following script and see if you can predict the result? What would the final stack look like?

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
    
    
    planets_stack = Stack()
    planets_stack.add("Mercury")
    planets_stack.add("Venus")
    planets_stack.add("Earth")
    planets_stack.add("Mars")
    planets_stack.add("Jupiter")
    planets_stack.add("Saturn")
    planets_stack.remove()
    planets_stack.remove()
    planets_stack.remove()
    planets_stack.add("Uranus")
    planets_stack.remove()
    planets_stack.remove()
    planets_stack.add("Neptune")
    
    for planet in planets_stack:
        print(planet)

##### Pondering

    Take a moment to think about the follwing challenge questions:
    
    1. What would be the outcome if the values are added to the front of the stack?
    2. What would happen if the stack removes the values from the front? would you be able to keep track of the succession of events?
    3. Code output: Mercury, Venus, Neptune

### LIFO

We would like to take a moment to explain what LIFO is. According
to [Tutorials Point](https://tutorialspoint.dev/data-structure/queue-data-structure/fifo-vs-lifo-approach-in-programming) 
, **The last in, first out(LIFO)** is a method for handling data structures where the last element is processed first and
the first element is processed last.

### Functionality

#### Push: Adding an element into the stack

Pushing or adding an element into the stack is done by appending the element to the back to the stack. That way, the
latest element is always removed first and older elements are moved to the front of the stack. It allows to backtrack or
undo operations and you can always return to a previous state.

Below is the code that adds a value to the stack. Notice that we are using append to add the value the
the back of the stack. 

        
            # Adds valid value to stack
            def add(self, value):
                if value:
                    self.stack.append(value)


##### Pondering

    Take a moment to think about the follwing challenge questions:
    
    1. What would be the outcome if the values are added to the front of the stack?
    2. Would it make sense to add the values randomly? 

#### Pop: Removing an element from the stack

Removing an element from the stack is done by removing the latest element added to the stack or the element at the top
of the stack. Removing the newest element added allows us to undo operations like the undo option in a text editor or
back button on a browser.

        # Removes value from stack
        def remove(self):
            if len(self.stack) > 0:
                return self.stack.pop()


##### Pondering

     Take a moment to think about the follwing challenge questions:
     
     1. What would be the outcome if the values are added to the front of the stack?
     2. Would you be able to go back in the same order you visited these pages?

#### Size: Getting the size of the stack

In order to get the size of the stack we can pass our data structure to the `len()` function.
The len() Python method returns the length of a list, string, dictionary, or any other iterable data format in Python.

    size = len(student_stack)
    print(size)

We can check if the stack is empty by doing a `==` comparison. 

    if len(student_stack) == 0:
        ... do abc task
    else:
        ... do something else

### Coding challenge #1

Imagine that you manage a warehouse and you are charge with the responsability of implementing a system that prioritises
the last product batches to enter the warehouse, while goods deposited previously on the pallet racking systems will be
stored until there is no other unit load in front of them. You recognize that this is a LIFO method and a stack is the
data structure to be used.

1. How would you keep track of the sequence of the batches?
2. How do you know what batch to dispatch next?
3. How would you print a list of all the batches?
4. How do you know what is the oldest batch in your inventory?

![Warehouse](images/warehouse.jpeg "Warehouse image")

### Coding challenge #2

You have been tasked to implement the back button of a browser in a new startup company and you are giving the following use case.

Imagine that you are a perspective student wanting
to apply to BYU-Idaho. Once you visit the help section, you are ready to go back to the application page. How can you do
that using the stack? Try to come up with with you own solution to put in practice what you have learned.

### Feedback

Please write your solutions to the use cases described above and feel free to email them
at <alexesca@byui.edu>. Compare your solution with the examples provided [here](warehouse.md) and [here](browser.md).

### Performance

| Operation      | Big O |  Implementation | 
| ----------- | ----------- | ----------- |
| Add      | O(1)       | .append(val) |
| Remove   | O(1)        | .pop() |
| Size   | O(1)        |   len(students_stack) |

### Do's and don'ts

#### When to use stacks

Implement in systems with homogeneous data, which do not lose value over time, don't change often or unexpectedly, and which do not expire.

#### When not to use stacks

Do not use stacks when you need to prioritize disposing or dispatching older products or elements. A FIFO method
implemented using a **queue** is your way to go.  
