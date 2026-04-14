class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            n = nums[i]
            if (target-n) in dictionary:
                j = dictionary[target-n]
                return [j,i]
            else:
                dictionary[nums[i]] = i