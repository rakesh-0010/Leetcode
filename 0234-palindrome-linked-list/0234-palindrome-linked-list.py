# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev_ll(self,cur):
        prev = None
        while cur != None:
            temp = cur.next
            cur.next = prev
            prev =cur
            cur = temp
        return prev

    def isPalindrome(self, head: ListNode | None) -> bool:
        slow = head
        fast =head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        mid = self.rev_ll(slow)
        cur = head

        while mid != None:
            if cur.val != mid.val:
                return False
            else:
                cur=cur.next
                mid = mid.next
        return True


            