class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for c in tokens:
            if c in '+-*/' and stack:
                a=int(stack.pop())
                b=int(stack.pop())
                if c=='+':
                    stack.append(a+b)
                elif c=='-':
                    stack.append(b-a)
                elif c=='*':
                    stack.append(a*b)
                else:
                    stack.append(b/a)
            else:
                stack.append(c)
        if stack:
            return int(stack.pop())

        