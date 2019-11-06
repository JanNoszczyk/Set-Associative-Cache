import logging
from abc import ABC, abstractmethod
from linked_list import Node, HashedLinkedList
logging.basicConfig(level=logging.DEBUG)


class Cache(ABC):
    """
    Abstract Cache class with put and get methods and an abstract method replace.
    """
    def __init__(self, size, number_of_ways):
        """
        :param size: The total number of cache entries
        :param number_of_ways: Number of cache entries per set
        """
        self.size = size
        self.number_of_ways = number_of_ways
        self.number_of_sets = int(size/number_of_ways)
        self.cache = [HashedLinkedList() for _ in range(self.number_of_sets)]
        self.key_type = None
        self.value_type = None

    def put(self, key, value):
        """
        Adds a new entry to the cache.
        :param key: key of the entry to be inserted
        :param value: value to be inserted
        """
        if not self.key_type:
            # Set the default key and value type the same as that of the first cache input
            self.key_type = type(key)
            self.value_type = type(value)
            logging.info("The default key type is {}, and default value type is {}."
                         .format(self.key_type, self.value_type))

        if type(key) == self.key_type and type(value) == self.value_type:
            set_number = hash(key) % self.number_of_sets
            current_set = self.cache[set_number]
            if len(current_set.dic) >= self.number_of_ways and key not in current_set.dic:
                # If the length of set exceeds the number of ways, follow the specified
                # replacement strategy to remove a node
                self.replace(current_set)
            if key in current_set.dic:
                # If the key already present, remove it and add it back again at the top of the list
                current_set.remove(current_set.dic[key])
            # Add the key, value pair at the top of the linked list
            n = Node(key, value)
            current_set.add(n)
            # Store the location of the node in a dictionary for quick access
            current_set.dic[key] = n

            logging.info("Successfully inserted the pair ({}, {})".format(key, value))

        else:
            raise Exception("The types of the key value pair ({}, {}) are different from the default types."
                            .format(key, value))

    def get(self, key):
        """
        Retrieves a value from the cache for a specified key. If the key is present, it will also be placed at the
        beginning of the linked list.
        :param key: The required key to find
        :return: The retrieved value
        """
        set_number = hash(key) % self.number_of_sets
        current_set = self.cache[set_number]
        if key in current_set.dic:
            n = current_set.dic[key]
            # Remove the node and add it back at the top of the linked list
            current_set.remove(n)
            current_set.add(n)
            return True, n.val

        logging.info("The key {} was not found in cache.".format(key))
        return False, None

    @abstractmethod
    def replace(self, current_set):
        """
        An abstract method that remove an entry from the cache after cache capacity has been exceeded.
        :param current_set: The cache set from which an entry is to be deleted
        :type current_set: HashedLinkedList
        """
        pass

    def print_contents(self):
        """
        Prints the current cache contents.
        """
        for i, current_set in enumerate(self.cache):
            sentence = "Set {}:".format(i)
            node = current_set.head.next
            while node != current_set.tail:
                sentence += " ({}, {})".format(node.key, node.val)
                node = node.next
            print(sentence)
