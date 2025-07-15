# Last updated: 7/15/2025, 5:50:42 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        sl = list(s)

        if len(nums) != len(sl):
            return True
        else:
            return False
        