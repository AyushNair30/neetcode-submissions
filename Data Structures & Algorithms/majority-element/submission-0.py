class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj=len(nums)/2
        freq=Counter(nums)
        for num in freq:
            if(freq[num]>=maj):
                return num