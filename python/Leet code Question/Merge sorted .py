# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
          # Dummy node start karne ke liye (final list ka head yahi hoga)
        dummy = ListNode()
        current = dummy

        # Jab tak dono lists me se koi empty nahi hoti
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1  # Chhoti value jodo
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next  # Next position pe jao

        # Agar koi list bach gayi ho to usse jod do directly
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        # Final list ka head dummy.next hoga (dummy ko skip karo)
        return dummy.next
        