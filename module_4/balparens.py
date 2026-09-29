from pythonds3.basic import Stack


def par_checker(symbol_string):
    s = Stack()
    for symbol in symbol_string:
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            s.pop()
    return s.is_empty()

print(par_checker("{ [ a + (b * c) ] - (d + e) }"))  

# add test cases here
# print(par_checker("()"))  # True
# print(par_checker("(())"))  # True
#print(par_checker("(()"))  # False
# print(par_checker("())"))  # False
# print(par_checker(")("))  # False
