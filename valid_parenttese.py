def isValid(s: str) -> bool:
    stack = []
    contains = {'(': ')', '{': '}', '[': ']'}
    if len(s) == 1:
        print('here is 5 line ', len(s))
        return False
    for i in s:
        if i in contains:
            stack.append(i)
        elif len(stack) == 0 or contains[stack.pop()] != i:
            return False
    return len(stack) == 0

print(isValid("([])"))