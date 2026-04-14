class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currentCount,maxCount = 0,0
        for x in nums:
            if x==1:
                currentCount+=1
            if currentCount > maxCount:
                maxCount = currentCount
            if x==0:
                currentCount = 0
        return maxCount
            