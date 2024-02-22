# ---------------------------------- Problem --------------------------------- #
# URL: https://leetcode.com/problems/reverse-linked-list/
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# ----------------------------------- Notes ---------------------------------- #
# recursive call will return sublist reversed
# so now need to append curr node to end
# base case if we get empty list to reverse
# [1,2,3,4,5]
# reversed_list - [5,4,3,2]
# then head is pointing at 1 - so next ref needs to be changed

# --------------------------------- Solution --------------------------------- #
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    reversed_sublist = self.reverseListRecursive(head.next)
    head.next.next = head
    head.next = None

    return reversed_sublist


# ----------------------------------- Notes ---------------------------------- #
# Need to keep track of prev and next and keep iterating until we reach the end
# at the end prev will be the new head
def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev_node, next_node = None, None

    while head:
        next_node = head.next
        head.next = prev_node

        prev_node = head
        head = next_node

    return prev_node
