# Last updated: 7/15/2025, 5:50:39 PM
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k = ""
        j = 0 
        for i in range(len(t)):
            if j < len(s) and s[j] == t[i]:
                k += t[i]
                j += 1

        return k == s


        