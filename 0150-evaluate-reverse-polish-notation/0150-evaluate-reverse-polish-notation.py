class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if (i=='+' or i=='-' or i=='*' or i=='/'):
                a=int(stack.pop())
                b=int(stack.pop())
                if i == '*':
                    stack.append(a * b)
                elif i == '/':
                    stack.append(int(b / a))
                elif i == '+':
                    stack.append(a + b)
                else:
                    stack.append(b - a)
            else:
                stack.append(i)
        return int(stack[-1])