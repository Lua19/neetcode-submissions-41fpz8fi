class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for x in range(len(nums)):
            ans.insert(x,nums[x])
            ans.append(nums[x])
        return ans