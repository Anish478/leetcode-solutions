# Last updated: 7/15/2025, 5:50:40 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = []
        f = []
        for i in range(len(nums)):
            if nums[i] == 0:
                k.append(i)
                f.append(nums[i])
        for j in reversed(k):
            nums.pop(j)
        nums.extend([0] * len(k))
        
        
        
            

        