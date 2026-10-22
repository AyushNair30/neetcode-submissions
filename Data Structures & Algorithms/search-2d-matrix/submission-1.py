class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c=len(matrix),len(matrix[0])
        top=0
        bottom=r-1
        while top<=bottom:
            midr=(top+bottom)//2
            if matrix[midr][-1]==target:
                return True
            elif matrix[midr][0]>target:
                bottom=midr-1
            elif matrix[midr][-1]<target:
                top=midr+1
            else:
                break
        if top>bottom:
            return False
        midr=(top+bottom)//2
        l,e=0,c-1
        while l<=e:
            mid=(l+e)//2
            if matrix[midr][mid]<target:
                l=mid+1
            elif matrix[midr][mid]>target:
                e=mid-1
            else:
                return True
        return False