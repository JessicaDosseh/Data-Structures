"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        # Create new_node
        new_node = ListNode(value)
        # 1. Add to empty list
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        # 2. Add to Nonempty list
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        # 3. Update length
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if self.head is None and self.tail is None:
            return None
        else:
            value = self.head.value
            self.head.delete()
            if self.head is self.tail:
                self.head = self.head.next
                self.tail = self.tail.prev
            else:
                self.head = self.head.next
            self.length -= 1
            return value

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        # Create new_node
        new_node = ListNode(value)
        # 1. Add to an empty list
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        # 2. Add to a Nonempty list
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        # 3. Update length
        self.length += 1

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if self.head is None and self.tail is None:
            return None
        else:
            value = self.tail.value
            self.tail.delete()
            if self.tail is self.head:
                self.head = self.head.next
                self.tail = self.tail.prev
            else:
                self.tail = self.tail.prev
            self.length -= 1
            return value

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if node is self.head:
            return
        value = node.value
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1
        self.add_to_head(value)

        '''
        if node is self.head:
            return
        self.delete(node)
        self.add_to_head(node.value)
        '''

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        if node is self.head:
            self.remove_from_head()
        else:
            node.delete()
            self.length -= 1
        self.add_to_tail(value)

        '''
        if node is self.tail:
            return
        self.delete(node)
        self.add_to_tail(node.value)
        '''

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """

    def delete(self, node):
        # delete does not need to return a value
        # delete can use the delete() method to reasign pointers

        # List is empty
        if self.head is None and self.tail is None:
            return None
        # List is NOT empty
        # List has 1 element
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        # List has +2 elements
        # delete head
        elif node is self.head:
            self.head = node.next
            node.delete()  # update prev and/or next pointers
        # delete tail
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        # delete item between head and tail
        else:
            node.delete()
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        # List is empty
        if self.head is None and self.tail is None:
            return None
        # List is Not empty
        # keep track of current node and max value
        current_node = self.head
        max_val = self.head.value
        # loop through doubly linked list
        while current_node:  # while current_node is not None:
            if max_val < current_node.value:
                max_val = current_node.value
            else:
                current_node = current_node.next
        return max_val
