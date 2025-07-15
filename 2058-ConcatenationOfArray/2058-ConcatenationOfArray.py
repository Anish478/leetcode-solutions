# Last updated: 7/15/2025, 5:50:30 PM
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[i])
        
        ans += ans
        return ans
               