# Last updated: 7/15/2025, 5:50:45 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()
        ns = ""
        for i in s:
            if i.isalnum():
                ns += i
                
        if ns == ns[::-1]:
            return True
        else:
            return False
        
            
        
        