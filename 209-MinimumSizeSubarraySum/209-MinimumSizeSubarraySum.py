# Last updated: 7/15/2025, 5:50:42 PM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        l = float('inf')
        L = 0

        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                l = min(R-L+ 1, l)
                total = total - nums[L]
                L+=1
        return 0 if l == float('inf') else l
        