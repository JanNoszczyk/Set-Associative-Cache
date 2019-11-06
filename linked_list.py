class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class HashedLinkedList(object):
    """
    The class implements a linked list to store the (key, value) pairs.
    Using a hashtable (dic) to store all nodes in the linked list allows O(1) lookup of elements. Removing and adding
    elements is also done in constant time.
    """
    def __init__(self):
        self.dic = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        n = node.next
        p = node.prev
        p.next = n
        n.prev = p

    def add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
