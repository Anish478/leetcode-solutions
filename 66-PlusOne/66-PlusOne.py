# Last updated: 7/15/2025, 5:50:48 PM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = "".join(str(i) for i in digits)
        num = int(s) + 1
        return [int(c) for c in str(num)]

            

        