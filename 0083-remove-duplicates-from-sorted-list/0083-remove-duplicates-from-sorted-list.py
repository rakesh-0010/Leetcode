# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if head == None:
            return None
        cur = head
        temp = head

        while temp != None:
            if cur.val == temp.val:
                temp = temp.next
            else:
                cur.next = temp
                cur = temp
        cur.next = temp
        return head
