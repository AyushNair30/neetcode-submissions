class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairsum={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in pairsum:
                return[pairsum[diff],i]
            else:
                pairsum[num]=i
