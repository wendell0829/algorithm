# Definition for singly-linked list.
# 合并2个升序链表,合并后仍为升序
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1:
            if list2:
                while True:
                    while True:
                        if list2.val<list1.val:
                            list2.next = list1
                            break
                        else:
                            list1 = list1.next


            return list1
        return list2


if __name__ == '__main__':
    n3 = ListNode(4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    n6 = ListNode(4)
    n5 = ListNode(3, n3)
    n4 = ListNode(1, n2)
    # n:ListNode = mergeTwoLists(n1, n4)

    n = n1
    while True:
        print(n.val)
        if n.next:
            n=n.next
        else:
            break