# Last updated: 7/15/2025, 5:50:44 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers) - 1
        

        while l< r:
            if numbers[l] + numbers[r] > target:
                r-=1
            elif numbers[l] + numbers[r] < target:
                l+=1
            else:
                return [l+1,r+1]