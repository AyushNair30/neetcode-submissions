class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check={}
        for i,num in enumerate(nums):
            check[num]=i
        for i,num in enumerate(nums):
            diff=target-num
            if diff in check and check[diff]!=i:
                return [i,check[diff]]