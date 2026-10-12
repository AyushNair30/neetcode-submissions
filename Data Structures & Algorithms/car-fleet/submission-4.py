class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car=sorted(zip(position,speed),reverse=True)

        ans=[]
        for i,s in car:
            t=(target-i)/s
            if not ans or t>ans[-1]:
                ans.append(t)
            else:
                continue
        return len(ans)