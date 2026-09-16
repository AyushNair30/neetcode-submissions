class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for c in range(len(nums)-2):
            i,j=c+1,len(nums)-1
            while(i<j):
                sum=nums[c]+nums[i]+nums[j]
                if(sum==0):
                    if [nums[c],nums[i],nums[j]] not in res:
                        res.append([nums[c],nums[i],nums[j]])
                if sum>0:
                    j-=1
                else:
                    i+=1
        return res