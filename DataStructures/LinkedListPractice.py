class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

    def prepend(self, value):
        # add a new node to the start of the list
        # create the new node
        # point its "next" to the current head
        # make "selfs" head this new node
        # but...we can early return if we know there is no current head
        if not self.head:
            self.head = Node(value)
            return

        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        # traverse the list until we get to the end
        # point ends next to this new node
        if not self.head:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def search(self, value):
        # traverse the list
        # check if that nodes value is the value we past here
        # return that node
        if not self.head:
            return None
        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next
        return None

    def remove(self, value):
        # traverse the list
        # if that nodes next value is the value we pass
        #   make next equal next next

        # to traverse
        # start at head
        # while the current node *has* a next
        #   check that next value
        #   move onto the next node (which is the node you just checked)

        # how does this work with removing the last node?
        # you're on the second last node,
        if self.head is None:
            return

        if self.head.value == value:
            if self.head.next:
                # need to check that there is a head.next
                self.head = self.head.next
            else:
                self.head = None
            return

        node = self.head
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return
            node = node.next

        raise ValueError("Value not found in the list.")

    def pop(self):
        # get the first node (which is head)
        # then remove head
        node = self.head
        self.remove(self.head.value)

        return node.value

    def insert(self, value, pos):
        # traverse the list
        # if some_index = pos
        #   add new node
        if self.head is None:
            self.head = Node(value)
            return

        if pos == 0:
            self.prepend(value)
            return

        index = 0
        node = self.head
        while node.next and index <= pos:
            if (pos - 1) == index:
                new_node = Node(value)
                new_node.next = node.next
                node.next = new_node
            index += 1
            node = node.next
        else:
            self.append(value)

    def size(self):
        # traverse the list
        # increment a counter for each step
        # return the counter
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

linked_list = LinkedList()
linked_list.prepend(1)
linked_list.prepend(2)
linked_list.prepend(3)
print(linked_list.to_list())
linked_list.remove(1)
print(linked_list.to_list())
linked_list.pop()
linked_list.insert(5, 0)
print(linked_list.size())
print(linked_list.to_list())
