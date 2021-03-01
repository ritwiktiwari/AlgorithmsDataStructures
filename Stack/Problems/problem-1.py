"""
Stack to balance brackets
"""

from Stack import Stack


def check(input_string: str) -> bool:
    _dict = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    stack = Stack()
    for i in input_string:
        if i in _dict.values():
            stack.push(i)
        elif i in _dict.keys():
            element = stack.pop()
            if element != _dict[i]:
                return False
        else:
            pass
    return True


print(check("abc{def} []"))
print(check("abc{def}pqrs]"))