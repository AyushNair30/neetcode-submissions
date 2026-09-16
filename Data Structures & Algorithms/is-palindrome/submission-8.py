class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        i=0
        j=len(s)-1
        while(i<j):
            while(i<j and s[i].isalnum()!=True):
                i+=1
            while(i<j and s[j].isalnum()!=True):
                j-=1
            if(s[i]!=s[j]):
                return False
            else:
                i+=1
                j-=1
        return True