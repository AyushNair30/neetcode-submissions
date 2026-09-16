class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s=""
        for letter in s:
            if letter.isalpha() or letter.isdigit():
                new_s+=letter.lower()
        print(new_s)
        i,j=0,len(new_s)-1
        while i<j:
            if new_s[i]!=new_s[j]:
                return False
            else:
                i+=1
                j-=1
        return True
        