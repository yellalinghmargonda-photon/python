def reverse(head, left, right):
    if not head or left == right:
        return head  # No change needed

    prev = None
    current = head

    # Move `current` to the `left` position, keeping track of `prev`
    for i in range(left - 1):
        prev = current
        current = current.next

    rev_start = prev  # Node before the sublist to be reversed
    rev_end = current  # The first node to be reversed
    next_node = None

    # Reverse the sublist
    for i in range(right - left + 1):
        temp = current.next
        current.next = next_node
        next_node = current
        current = temp

    # Connect the reversed sublist back to the main list
    if rev_start:
        rev_start.next = next_node
    else:
        head = next_node  # If `left` is 1, update the head

    rev_end.next = current  # Connect the last node of reversed part to `current`
    return head  # Return the new head
