class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = [x.lower() for x in s if x.isalnum()]
        l = 0
        r = len(alphanum)-1
        while (l < r):
            if alphanum[l] == alphanum[r]:
                l +=1
                r -=1
            else:
                return False
        return True