# Last updated: 7/15/2025, 5:50:35 PM
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i

        return -1
        