# Last updated: 7/15/2025, 5:50:52 PM
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = {')':'(', '}': "{",']':'['}

        for i in s:
            if i in close:
                if stack and stack[-1] == close[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
        