import logging
from cache_implementations import LRUCache, MRUCache, CustomCache


def create_new_cache(size: int, number_of_ways: int, strategy: str = 'LRU', replacement_algorithm=None) -> object:
    """

    :param size:
    :param number_of_ways:
    :param strategy:
    :param replacement_algorithm:
    :return:
    """
    if size % number_of_ways == 0:
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
