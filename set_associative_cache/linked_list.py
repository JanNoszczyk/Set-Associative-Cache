class Node(object):
    """
    Node class used to build a HashedLinkedList.
    """
    def __init__(self, key, val):
        """
        :param key: Key for the node entry
        :param val: Value for the entry
        """
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class HashedLinkedList(object):
    """
    The class implements a doubly linked list to store the (key, value) pairs. This allows removing and adding
    elements in constant time.
    Using a hashtable (dic) to store all nodes in the linked list allows O(1) lookup of elements.
    """
    def __init__(self):
        self.dic = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        """
        Removes a node from the linked list.
        :param node: Node to be removed
        :type node: Node
        """
        n = node.next
        p = node.prev
        p.next = n
        n.prev = p

    def add(self, node):
        """
        Adds a node at the end of the linked list.
        :param node: Node to be added
        :type node: Node
        """
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
