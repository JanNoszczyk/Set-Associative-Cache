from cache_implementations import LRUCache, MRUCache, CustomCache


def create_new_cache(size: int, number_of_ways: int, strategy: str = 'LRU', replacement_algorithm=None) -> object:
    """
    Creates a new Cache object that uses the specified node replacement strategy.
    :param size: The total number of cache entries
    :param number_of_ways: Number of cache entries per set
    :param strategy: Strategy to remove an entry from the cache set after its size limit has been exceeded
    :param replacement_algorithm: User defined node replacement method (Only used when strategy='custom')
    :return: Cache object for the specified replacement strategy
    """
    if size % number_of_ways == 0:
        # The number of ways (entries per cache set) needs to be a multiple of the cache size
        if strategy == 'LRU':
            return LRUCache(size, number_of_ways)
        elif strategy == 'MRU':
            return MRUCache(size, number_of_ways)
        elif strategy == 'custom':
            if callable(replacement_algorithm):
                return CustomCache(size, number_of_ways, replacement_algorithm)
            else:
                raise Exception("The specified replacement algorithm is incorrect.")
        else:
            raise Exception("The provided strategy name ({}) is incorrect. It needs be either 'LRU', 'MRU' or 'custom'"
                          .format(strategy))
    else:
        raise Exception("The provided number of ways ({}) is not a multiple of cache size ({})."
                      .format(number_of_ways, size))
