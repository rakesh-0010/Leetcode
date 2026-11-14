# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        cur=head
        stack=[]
        while cur != None:
            stack.append(cur.val)
            cur=cur.next
        stack.reverse()
        cur=head
        k=0
        while cur != None:
            if(cur.val != stack[k]):
                return False
            else:
                cur=cur.next
                k+=1
        return True


            