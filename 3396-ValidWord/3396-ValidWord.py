# Last updated: 7/15/2025, 5:50:27 PM
class Solution:
    def isValid(self, word: str) -> bool:
        vow = ['a','e','i','o','u','A','E','I','O','U']
        c = 0
        v = 0

        if len(word) >= 3 and word.isalnum():
            for ch in word:
                if ch.isdigit():       
                    continue
                elif ch in vow:         
                    v += 1
                else:                  
                    c += 1

        if c > 0 and v > 0 and len(word) >= 3 and word.isalnum():
            return True
        else:
            return False
