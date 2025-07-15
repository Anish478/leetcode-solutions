# Last updated: 7/15/2025, 5:50:32 PM
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = {}
        a = []
        for i in range(len(arr)):
            if arr[i] not in d:
                d[arr[i]] = 1
            else:
                d[arr[i]]+= 1 
        for h in d:
            if(d[h] == h):
                a.append(h)
        return max(a) if a else -1
