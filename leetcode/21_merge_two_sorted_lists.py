"""

21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        li = []
        while l1:
            li.append(l1.val)
            l1 = l1.next
        while l2:
            li.append(l2.val)
            l2 = l2.next

        if not li:
            return None

        li.sort()
        result = ListNode(li.pop(0))
        temp = result
        while li:
            val = li.pop(0)
            temp.next = ListNode(val)
            temp = temp.next

        return result