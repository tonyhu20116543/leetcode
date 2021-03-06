# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        p = head
        flag = 0
        while l1 is not None or l2 is not None or flag != 0:
            a = l1.val if l1 is not None else 0
            b = l2.val if l2 is not None else 0
            sum = a + b + flag
            flag = sum // 10
            
            node = ListNode(sum % 10)
            p.next = node
            p = p.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            
        return head.next
        
