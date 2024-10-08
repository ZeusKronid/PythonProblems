# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = temp = ListNode(0)
        while l1 != None and l2 != None: #1

            if l1.val < l2.val: #2
                temp.next = l1 #3
                l1 = l1.next #4
            else: 
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 or l2  #5
        return dummy.next #6
            



sol = Solution()
sol.mergeTwoLists(ListNode(val = 1, next = ListNode(val= 2, next = ListNode(val = 4, next = None))), ListNode(val= 1, next= ListNode(val =  3, next =  ListNode(val =  4, next = None))))
