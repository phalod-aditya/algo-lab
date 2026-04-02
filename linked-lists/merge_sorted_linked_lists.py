# https://leetcode.com/problems/merge-two-sorted-lists/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr = list1
        curr2 = list2

        a1 = []
        a2 = []

        # convert list1 to a1

        while curr is not None:

            a1.append(curr.val)
            curr = curr.next

        # convert list2 to a2
        
        while curr2 is not None:

            a2.append(curr2.val)
            curr2 = curr2.next

        # merge and sort a1, a2

        merged = a1 + a2

        merged.sort()
        print(merged)

        # if empty, return null

        if len(merged) == 0:
            return None

        # merged to linked list

        head = ListNode(merged[0])
        current = head

        for i in merged[1:]:
            new_node = ListNode(i)
            current.next = new_node
            current = new_node

        return head
