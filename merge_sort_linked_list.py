# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge_sort(head):
            if not head or head.next is None:
                return head
            slow = head
            fast = head
            while (fast and fast.next):
                fast = fast.next.next
                prev = slow
                slow = slow.next
            prev.next = None
            low, high = head, slow
            left_list = merge_sort(low)
            right_list = merge_sort(high)
            return perform_merging(left_list, right_list)

        def perform_merging(list1, list2):
            dummy = ListNode()
            head = dummy
            while (list1 and list2):
                if list1.val < list2.val:
                    head.next = list1
                    list1 = list1.next
                else:
                    head.next = list2
                    list2 = list2.next
                head = head.next
            if list1:
                head.next = list1
            if list2:
                head.next = list2
            return dummy.next

        return merge_sort(head)
