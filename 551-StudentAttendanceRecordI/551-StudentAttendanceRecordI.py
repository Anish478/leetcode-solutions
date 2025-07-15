# Last updated: 7/15/2025, 5:50:38 PM
class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A')<2 and 'LLL' not in s:
            return True
        else:
            return False