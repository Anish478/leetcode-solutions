# Last updated: 7/15/2025, 5:50:29 PM
class Solution:
    def possibleStringCount(self, word: str) -> int:
        count = 0
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                count+= 1
            else:
                pass
        return count+1



        