# Last updated: 7/15/2025, 5:50:51 PM
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        u = sorted(set(nums))
        nums[:len(u)] = u
        return len(u)