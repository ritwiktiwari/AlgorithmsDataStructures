class Stack:
    def __init__(self, length=None) -> None:
        """Initialize a stack"""

        self.stack = list()
        self.length = length
        self.elements = 0

    def push(self, value):
        """Insert item into the stack"""

        if not self.length:
            self.stack.append(value)
        else:
            if self.length > self.elements:
                self.stack.append(value)
            else:
                raise Exception("Stack is full")
        self.elements += 1

    def pop(self):
        """Remove and return the last item inserted in the stack"""

        if self.is_empty():
            return None
        else:
            self.elements -= 1
            return self.stack.pop()

    def top(self):
        """Return the last item inserted in the stack"""

        if not self.is_empty():
            return self.stack[-1]
        return None

    def size(self):
        """Return the number of items in the stack"""

        return self.elements

    def is_empty(self):
        """Check whether the stack has any items stored or not"""

        if self.elements == 0:
            return True
        return False

    def verbose(self):
        """Returns all the stack info in a dict"""
        temp = {
            'stack': self.stack,
            'elements': self.elements,
            'length': "Dynamic" if self.length is None else self.length
        }
        return temp

    def __str__(self):
        return ' '.join(str(v) for v in self.stack)
