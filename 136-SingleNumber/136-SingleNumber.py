# Last updated: 7/15/2025, 5:50:45 PM



class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums) - 1, 2):  # Step by 2, check pairs
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]