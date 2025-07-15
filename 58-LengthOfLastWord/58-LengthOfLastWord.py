# Last updated: 7/15/2025, 5:50:49 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split()
        return len(a[-1])