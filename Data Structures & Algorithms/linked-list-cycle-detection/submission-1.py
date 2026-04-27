# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None: return False
        hare = head
        tort = head
        while (hare != None and hare.next != None):
            hare = hare.next.next
            tort = tort.next
            if hare == tort: return True
        return False