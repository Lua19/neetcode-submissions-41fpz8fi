
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        digits = {}
        for x in nums:
            if x in digits:
                digits[x] = digits[x] + 1
            else:
                digits.setdefault(x,1)
        return max(digits, key=digits.get)