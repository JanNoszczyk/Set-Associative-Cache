from cache_class import Cache


class LRUCache(Cache):
    def replace(self, current_set):
        lru_node = current_set.head.next
        current_set.remove(lru_node)
        del current_set.dic[lru_node.key]


class MRUCache(Cache):
    def replace(self, current_set):
        mru_node = current_set.tail.prev
        current_set.remove(mru_node)
        del current_set.dic[mru_node.key]


class CustomCache(Cache):
    def __init__(self, size, number_of_ways, replacement_algorithm):
        super().__init__(size, number_of_ways)
        self.replacement_algorithm = replacement_algorithm

    def replace(self, current_set):
        self.replacement_algorithm(current_set)
