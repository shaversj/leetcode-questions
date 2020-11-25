# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        tail = head

        while True:
            if l1 is None:
                tail.next = l2
                break
            if l2 is None:
                tail.next = l1
                break

            if l1.val >= l2.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next

            tail = tail.next

        print(self.print_list(tail.next))
        return head.next

    def print_list(self, l5: ListNode):
        while l5:
            print(l5.val, end=" ")
            l5 = l5.next

l1 = ListNode(val=1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
# l1 = ListNode(1).next(ListNode(2).next(ListNode(4)))
# l2 = ListNode(1).next(ListNode(3).next(ListNode(4)))

s = Solution()
ans = s.mergeTwoLists(l1, l2)
s.print_list(ans)
