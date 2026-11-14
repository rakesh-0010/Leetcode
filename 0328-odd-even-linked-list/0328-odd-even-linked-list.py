# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head == None or head.next == None:
            return head
        temp=[]
        odd = head
        while odd != None and odd.next != None:
            temp.append(odd.val)
            odd=odd.next.next
        if odd != None:
            temp.append(odd.val)
        even = head.next
        while even != None and even.next != None:
            temp.append(even.val)
            even=even.next.next
        if even != None:
            temp.append(even.val)
        cur = head
        k=0
        while cur != None :
            cur .val = temp[k]
            cur = cur.next
            k+=1
        return head