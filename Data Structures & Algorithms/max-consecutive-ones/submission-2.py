class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        curMax = 0
        for x in nums:
            if x==1:
                curMax+=1
                c = max(c,curMax)
            else:
                curMax = 0
                c = max(c,curMax)
        return c
            