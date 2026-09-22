from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = deque()

        for item in tokens:
            if item == '+':   
                top_num = stack.pop()
                top_next_num = stack.pop()
                stack.append(top_next_num + top_num)

            elif item == '-':
                top_num = stack.pop()
                top_next_num = stack.pop()
                stack.append(top_next_num - top_num)
            elif item == '*':
                top_num = stack.pop()
                top_next_num = stack.pop()
                stack.append(top_next_num * top_num)
                
            elif item == '/':
                top_num = stack.pop()
                top_next_num = stack.pop()
                stack.append(int(top_next_num / top_num))
            
            else:
                stack.append(int(item))
            
        return stack[-1]



        