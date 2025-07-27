#  Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                # Duplicate node found, skip it
                current.next = current.next.next
            else:
                # Move to next unique node
                current = current.next
        
        return head