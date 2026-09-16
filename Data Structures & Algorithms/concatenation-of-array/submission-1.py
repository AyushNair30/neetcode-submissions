class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        count=2
        while(count):
            for i in range(len(nums)):
                ans.append(nums[i])
            count-=1
        return ans