#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        if self.head is None:
            return True
        else:
            return False

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        len = 0
        for item in self.items():
            len += 1
        # Running time: O(n) since it is iterating through all the items.

        return len

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        NewNode = Node(item)
        if self.is_empty():
            self.head = NewNode
            self.tail = NewNode
            return
        else:
            self.tail.next = NewNode
            self.tail = NewNode
        # O(1)  - Change .tail.next and .tail

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        NewNode = Node(item)

        if self.is_empty():
            self.head = NewNode
            self.tail = NewNode
        else:
            NewNode.next = self.head
            self.head = NewNode

        # O(1) - change .head and .newnode.next

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        node = self.head
        while node is not None:
            if quality(node.data) is True:
                return node.data
            else:
                node = node.next

        return None
        # Best case: 0(1) when the node we are looking for is the head node. it returns after first iterations
        # Worst case: O(N) when the node we are looking for is the tail node, or is not in the list because it will take whole iterations

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        node = self.head
        prev = None
        word_found = False

        while node is not None:
            if node.data == item:
                word_found = True
                if self.head is node:
                    self.head = node.next
                else:
                    prev.next = node.next
                if self.tail is node:
                    self.tail = prev
                node = None
                # self.length -= 1
                return
            else:
                prev = node
                node = node.next

        if word_found == False:
            raise ValueError('Item not found: {}'.format(item)) # never found item

        # Best case: 0(1) when the node we are deleting for is the head node. it returns after first iterations
        # Worst case: O(N) when the node we are looking for is the tail node, or is not in the list because it will take whole iterations

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
