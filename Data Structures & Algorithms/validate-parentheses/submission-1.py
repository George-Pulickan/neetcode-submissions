from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:


        length = len(s)
        stack = deque()

        for i in range(length):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])

            elif len(stack) == 0:
                return False
            
            elif s[i] == ')' or s[i] == '}' or s[i] == ']':
                if s[i] == ')' and stack[-1] == '(':
                    stack.pop()
                elif s[i] == '}' and stack[-1] == '{':
                    stack.pop()
                elif s[i] == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False


        