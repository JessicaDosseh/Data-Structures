# a class that represents the individual elements in the Linked List
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # what attributes do we need?
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        # Create a new Node
        new_node = Node(value)
        if self.head is None:
            # update head and tail attributes
            self.head = new_node
            self.tail = new_node
        else:
            # set next_node of new Node to the head
            new_node.set_next_node(self.head)
            # update head attribute
            self.head = new_node

    def add_to_tail(self, value):
        # Create a new Node
        new_node = Node(value)
        # 1. Linked List is empty
        if self.head is None:
            # update head and tail attributes
            self.head = new_node
            self.tail = new_node

        # 2. Linked List is NOT empty
        else:
            # update next_node of tail
            self.tail.set_next_node(new_node)
            # update self.tail
            self.tail = new_node

    def remove_head(self):
        # empty list
        if self.head is None:
            return None
        # else, return VALUE of the old head
        else:
            ret_value = self.head.get_value()
            # list with 1 element
            if self.head == self.tail:
                self.head = None
                self.tail = None
            # list with +2 elements
            else:
                self.head = self.head.get_next_node()
            return ret_value

    def remove_tail(self):
        # List is empty return None
        if self.head is None:
            return None
        # List is NOT empty
        # List with 1 emelent
        elif self.head == self.tail:
            # save temp value of tail
            temp_value = self.head.get_value()
            self.head = None
            self.tail = None
            return temp_value
        # List with +2 element
        else:
            # save temp value of tail
            temp_value = self.tail.get_value()
            # refrence temp node
            current_node = self.head
        # while node.get_next_node() is not tail loop through
        while current_node.get_next_node() is not self.tail:
            current_node = current_node.get_next_node()
        # update ointer of temp node (prev_tail) to None
        self.tail = current_node
        self.tail.set_next_node(None)
        self.tail = current_node
        return temp_value

    def contains(self, value):
        # loop through Linked List until next pointer is None
        cur_node = self.head
        while cur_node is not None:
            # if we find 'value'
            if cur_node.get_value() == value:
                return True
        return False

    def get_max(self):
        cur_node = self.head
        if self.head == None:
            return None
        else:
            # Initializing mac with head's value
            max = self.head.value
            while cur_node is not None:
                # if cur_node value is greater than max
                # then replace value of max with cur_node value
                if max < cur_node.value:
                    max = cur_node.value
                cur_node = cur_node.get_next_node()
            print("Maximum value: " + str(max))
