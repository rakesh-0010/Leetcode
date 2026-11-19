# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        d={}
        cur1=headA
        while cur1!=None:
            d[cur1]=1
            cur1=cur1.next
        cur2=headB
        while cur2 !=None:
            if cur2 in d:
                return cur2
            else:
                cur2=cur2.next
        return None