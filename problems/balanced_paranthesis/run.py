### Solution 1
from stack import Stack

def is_open_paran(ch):
    return ch in ['(', '{', '[']

def is_balanced(open_br, close_br):
    if open_br == '(' and close_br == ')':
        return True
    
    if open_br == '{' and close_br == '}':
        return True

    if open_br == '[' and close_br == ']':
        return True

    return False

def balance_check(items):
    open_stack = Stack()

    for ch in items:
        if is_open_paran(ch):
            open_stack.push(ch)
        else:
            open_bracket = open_stack.pop()
            if not is_balanced(open_bracket, ch):
                return False
    if open_stack.isEmpty():
        return True
    else:
        return False