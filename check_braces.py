expressions = [")(){}","[]({})","([])","{()[]}","([)]"]

def check_braces(expressions):
    startbraces = set('([{')
    matchingbraces = set([('(', ')'), ('[', ']'), ('{', '}')])
    stack = []
    subset = 0
    for subset in range(len(expressions)):
        if len(expressions[subset]) % 2 != 0:
            print 0
         
        for char in expressions:
            if char in startbraces:
                stack.append(char)
            else:
                if len(stack) == 0:
                    print 0
                lastchar = stack.pop()
                if (lastchar, char) not in matchingbraces:
                    print 0
                else:
                    print 1
                    
check_braces(expressions)