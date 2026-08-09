"""
There are two ways to implement a stack in Python: using a list or by using the deque class from the collections module.
We will implement a stack using a list in this example. A stack is a linear data structure that follows the Last In First Out (LIFO) principle,
meaning that the last element added to the stack will be the first one to be removed.
"""


def stack_operations() : 

    """For the stack we can use List because both append() and pop() operations are O(1) in average case.
    While when we will see Queue it must use deque because append() and pop() operations are O(1) in average case for deque but O(n) for list.
    """
    # define a stack using a list
    stack = []

    # adding elements to the stack
    stack.append(1)
    stack.append(2)
    stack.append(3)

    # removing elements from the stack
    print(stack.pop())  # Output: 3
    print(stack.pop())  # Output: 2

    # checking the top element of the stack
    print(stack[-1])  # Output: 1

    # length of the stack
    print(len(stack))  # Output: 1

if __name__ == "__main__":
    stack_operations()