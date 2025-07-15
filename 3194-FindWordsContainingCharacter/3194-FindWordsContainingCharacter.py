# Last updated: 7/15/2025, 5:50:28 PM
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        s= []
        for i in range(len(words)):
            if x in words[i]:
                s.append(i)
        return s