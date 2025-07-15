# Last updated: 7/15/2025, 5:50:50 PM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            else:
                nums.append(target)
                nums.sort()
                for i in range(len(nums)):
                    if target == nums[i]:
                        return i        