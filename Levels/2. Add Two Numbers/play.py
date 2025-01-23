from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode{{val: {self.val}, next: {repr(self.next)}}}"


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy node to start the result list
        current = dummy  # Pointer to build the result list
        carry = 0  # Initialize carry to 0

        while l1 or l2 or carry:
            # Get values from l1 and l2, or 0 if they're None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum and the new carry
            total = val1 + val2 + carry
            carry = total // 10  # Carry is the tens digit
            new_val = total % 10  # New node value is the ones digit

            # Create a new node for the sum and move the pointer
            current.next = ListNode(new_val)
            current = current.next

            # Move to the next nodes in l1 and l2, if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next  # Return the node following the dummy as the head

if __name__ == '__main__':
    # Helper function to create a linked list from a list of integers
    def create_linked_list(values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        return head


    # Helper function to print linked list as a list
    def print_linked_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result


    # Input linked lists
    l1 = create_linked_list([2, 4, 3])  # Represents 342
    l2 = create_linked_list([5, 6, 4])  # Represents 465

    # Add two numbers
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    # Print result linked list
    print(print_linked_list(result))