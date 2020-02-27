from slime.data_structures.nodes.list_node import ListNode
from time import time


class LinkedList(object):
    """
    This is a generic linked list that tracks both a head and tail node.
    """

    def __init__(self, items=None):
        self.length = 0
        self.head = None
        self.tail = None
        if isinstance(items, (list, tuple)):
            for item in items:
                self.add_item(item)

    def _add_if_length_0_(self, data):
        self.head = self.tail = ListNode(data)

    def _add_if_length_1_(self, data):
        """
        Add a new node to the list, if the length of the list is
        equal to one.

        :param obj data: A data of any type
        :return: None
        """
        self.head.next = self.tail = ListNode(data)

    def _add_if_length_gt_1_(self, data):
        self.tail.next = self.tail = ListNode(data)

    def add_item(self, data):
        if self.length == 0:
            self._add_if_length_0_(data)
        elif self.length == 1:
            self._add_if_length_1_(data)
        else:
            self._add_if_length_gt_1_(data)
        self.length += 1

    def _del_head_(self):
        """
        Delete the head of the list, if the data of the head
        is the value to be deleted
        :return: None
        """
        cur = self.head
        self.head = self.head.next
        cur.data = None
        cur.next = None

    def _del_tail_(self):
        """
        Delete the node pointed to by tail.
        """
        # Assign an iterator variable to point to the current head
        cur = self.head

        # Since we do not know where the previous node is,
        # we must iterate over the list.
        while cur.next != self.tail:
            cur = cur.next

        # Now we need to assign the current tail to a tmp variable
        # in order to cleanup data
        tmp = cur.next

        # Then set the tail to be the previous node
        self.tail = cur

        # Cleanup data for security's sake
        self.tail.next = None
        tmp.data = None
        tmp.next = None

    def _del_node_(self, data):
        before = self.head
        del_node = None
        while before is not None:
            if before.next.data == data:
                del_node = before.next
                break
            before = before.next
        after = del_node.next
        before.next = after
        del_node.data = None
        del_node.next = None

    def del_item(self, data):
        if self.length == 0:
            return
        if data == self.head.data:
            self._del_head_()
        elif data == self.tail.data:
            self._del_tail_()
        else:
            self._del_node_(data)
        self.length -= 1

    def print_list(self):
        cur = self.head
        string = ""
        while cur is not None:
            string = f"{string} {cur.data}"
            cur = cur.next
        print(string)


if __name__ == '__main__':
    # Testing the class (Use Python 3.6+)
    MAX_NUMBERS = 5000000
    my_list2 = list(range(0, MAX_NUMBERS, 1))

    print(f"Creating linked list with {MAX_NUMBERS} integers as data...")

    init_time = time()
    llist = LinkedList(my_list2)
    create_time = time()
    creation_time = (create_time - init_time)/60

    start_time = time()
    for x in range(2000, MAX_NUMBERS, 1):
        llist.del_item(x)
    del_time = time()
    delete_time = (del_time - start_time)/60
    end_time = time()
    print(f"Initializing: {creation_time} minutes")
    print(f"Deletion: {delete_time} minutes")
    print(f"Total: {(end_time - init_time) / 60} minutes. ")
    llist.print_list()
    print(f"Final Length: {llist.length}")
