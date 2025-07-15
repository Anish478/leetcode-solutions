# Last updated: 7/15/2025, 5:50:51 PM
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        tmp = []
        for i in range(len(nums)):
            if nums[i] == val:
                tmp.append(nums[i])
            
        for i in tmp:
            nums.remove(i)
        return len(nums)
