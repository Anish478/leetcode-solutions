# Last updated: 7/15/2025, 5:50:48 PM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = bin(int(a, 2) + int(b, 2))
        return sum[2:]
