import pythonds3

def conv_stack(num, base):
    remstack = pythonds3.Stack()
    while num > 0:
        rem = num % base
        remstack.push(rem)
        num = num // base

    new_string = ""
    while not remstack.is_empty():
        new_string += str(remstack.pop())
    return new_string