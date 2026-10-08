class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        ans=[None]*len(temperatures)

        stack.append(0)

        for i in range(1,len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                check=stack.pop()
                ans[check]=i-check
            stack.append(i)
        while stack:
            ans[stack.pop()]=0
        return ans