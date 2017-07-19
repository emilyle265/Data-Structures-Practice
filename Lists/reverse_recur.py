def reverse_linked_list(node, prev=None):
    if node.next is None:
        node.next = prev
        return node
    root_node = reverse_linked_list(node.next, node)
    node.next = prev
    return root_node