

class ListNode(object):
    """
    Node class for creating node objects for a linked list
    """

    def __init__(self, data, previous_node=None, next_node=None):
        super(ListNode, self).__init__()
        self.data = data
        self.previous = previous_node
        self.next = next_node

