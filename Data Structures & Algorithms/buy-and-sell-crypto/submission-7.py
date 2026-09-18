class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        i=0
        for j in range(1,len(prices)):
            currp=0
            if prices[j]<prices[i]:
                i=j
            if prices[j]>prices[i]:
                currp=prices[j]-prices[i]
                j+=1
            maxp=max(maxp,currp)
        return maxp
