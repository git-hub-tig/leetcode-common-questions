"""
Question:
Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        end = len(lists) - 1
        while end > 0:
            begin = 0
            while begin < end:
                lists[begin] = self.merge2Lists(lists[begin], lists[end])
                begin += 1
                end -= 1
        return lists[0]

    def merge2Lists(self, l1, l2):
        dummyHead = ListNode(0)
        p = dummyHead
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return dummyHead.next


if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    res = Solution().mergeKLists(lists)
    print(res)
