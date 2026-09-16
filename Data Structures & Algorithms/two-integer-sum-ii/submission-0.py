class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res=[]
        i,j=0,len(numbers)-1
        while(i<j):
            sum=numbers[i]+numbers[j]
            if sum==target:
                res.append(i+1)
                res.append(j+1)
                return res
            elif sum>target:
                j-=1
            else:
                i+=1