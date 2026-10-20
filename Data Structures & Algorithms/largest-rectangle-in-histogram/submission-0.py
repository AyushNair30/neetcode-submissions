class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        amax=0
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                index,height=stack.pop()
                amax=max(amax,height*(i-index))
                start=index
            stack.append((start,h))
        
        for i,h in stack:
            amax=max(amax,h*(len(heights)-i))
        return amax

