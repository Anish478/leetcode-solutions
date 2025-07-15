# Last updated: 7/15/2025, 5:50:38 PM
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        t= 0
        self.l = []
        for i in range(len(nums)):
            
            t+=nums[i]
            self.l.append(t)


        

    def sumRange(self, left: int, right: int) -> int:
        prer = self.l[right]
        prel = self.l[left-1] if left >0 else 0
        return (prer -prel) 

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)