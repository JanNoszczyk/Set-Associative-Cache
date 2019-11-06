from cache_class import Cache


class LRUCache(Cache):
    """
    Cache class that uses LRU (Least Recently Used) replacement.
    """
    def replace(self, current_set):
        """
        Deletes a node using the LRU replacement method.
        :param current_set: Cache set to delete the node from
        :type current_set: HashedLinkedList
        """
        lru_node = current_set.head.next
        current_set.remove(lru_node)
        del current_set.dic[lru_node.key]


class MRUCache(Cache):
    """
    Cache class that uses MRU (Most Recently Used) replacement.
    """
    def replace(self, current_set):
        """
        Deletes a node using the MRU replacement method.
        :param current_set: Cache set to delete the node from
        :type current_set: HashedLinkedList
        """
        mru_node = current_set.tail.prev
        current_set.remove(mru_node)
        del current_set.dic[mru_node.key]


class CustomCache(Cache):
    """
    Cache class that uses a custom replacement method.
    """
    def __init__(self, size, number_of_ways, replacement_algorithm):
        """
        :param size: The total number of cache entries
        :param number_of_ways: Number of cache entries per set
        :param replacement_algorithm: Custom method to delete a node from a cache set after its size limit
        has been exceeded. It needs to be a callable function provided by the user.
        """
        super().__init__(size, number_of_ways)
        self.replacement_algorithm = replacement_algorithm

    def replace(self, current_set):
        """
        Deletes a node using a custom, user defined, replacement method.
        :param current_set: Cache set to delete the node from
        :type current_set: HashedLinkedList
        """
        self.replacement_algorithm(current_set)
