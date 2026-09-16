class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol=0
        i,j=0,len(heights)-1
        while(i<j):
            curr=(j-i)*min(heights[i],heights[j])
            max_vol=max(max_vol,curr)

            if heights[i]>heights[j]:
                j-=1
            elif heights[j]>heights[i]:
                i+=1
            else:
                i+=1
        return max_vol
        