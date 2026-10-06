class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        check={')':'(','}':'{',']':'['}

        for c in s:
            if c in check:
                if stack and check[c]==stack.pop():
                    continue
                else:
                    return False
            else:
                stack.append(c)
        return not stack
                    