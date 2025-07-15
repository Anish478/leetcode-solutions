# Last updated: 7/15/2025, 5:50:32 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        s = ""
        while head is not None:
            s+= str(head.val)
            head = head.next
        d = int(s,2)
        return d

            
            
        
        