# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        # reverse second half
        slow.next = None # have to set this to None to properly break the links between first and second lists or else will have a LL cycle that infinitely loops
        prev = None
        print("finding middle works")
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        # merge two halfs
        first = head
        second = prev
        print("reverse second half works")

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1 
            second = temp2


