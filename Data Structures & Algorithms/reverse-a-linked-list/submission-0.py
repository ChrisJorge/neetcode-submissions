# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Get the head of the linked list
        CurrentNode = head
        # Get the value of the node before the head (None)
        PreviousNode = None
        # Loop through the linked list until the currentNode is None
        while CurrentNode:
            # Create a temporary variable to hold the link to the rest of the list
            TemporaryNode = CurrentNode.next
            # Assign the next variable of the current node to the previous node
            CurrentNode.next = PreviousNode
            # Assign the previous node to the current node
            PreviousNode = CurrentNode
            # Assign the current node to the temporary value
            CurrentNode = TemporaryNode
        
        # Return PreviousNode as it is the new head
        return PreviousNode
            
