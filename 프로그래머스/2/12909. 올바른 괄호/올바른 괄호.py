def solution(s):
    answer = True
    stack = []

    for parentheses in s: 
        if parentheses == "(": 
            stack.append(parentheses) 
        else: 
            if stack and stack[-1] == "(": 
                stack.pop()
            else:
                return False 

    return len(stack) == 0 