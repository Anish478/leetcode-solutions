# Last updated: 7/15/2025, 5:50:34 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1