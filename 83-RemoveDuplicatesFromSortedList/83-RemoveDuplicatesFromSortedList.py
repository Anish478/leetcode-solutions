# Last updated: 7/15/2025, 5:50:47 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp and temp.next:
            if temp.val != temp.next.val:
                temp = temp.next
            else:
                temp.next = temp.next.next
        return head
        