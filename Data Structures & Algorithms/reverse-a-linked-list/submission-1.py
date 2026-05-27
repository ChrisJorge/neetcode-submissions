# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a variable for previous Node, set it to Null
        previousNode = None
        # Create a variable for the current Node and set it to head
        currentNode = head

        # Loop through the nodes while the current node is not Null
        while currentNode:
            # Create a temporary node to hold the link to the rest of the list
            tempNode = currentNode.next
            # Set the currentNodes.next to the previous Node
            currentNode.next = previousNode
            # Set the previousNode to the current Node
            previousNode = currentNode
            # Set the current node to the temporary Node
            currentNode = tempNode
        
        # return the previous Node
        return previousNode