from unittest import TestCase
from cache import create_new_cache
from cache_implementations import LRUCache, MRUCache, CustomCache


class TestCache(TestCase):

    def test_create_new_cache(self):
        """
        Test the output of create_new_cache with different strategy values
        """
        self.assertEqual(type(create_new_cache(2, 1)), LRUCache)
        self.assertEqual(type(create_new_cache(2, 1, 'MRU')), MRUCache)
        self.assertEqual(type(create_new_cache(2, 1, 'custom', lambda x: x)), CustomCache)

        # 'Not a function' is not a callable replacement-algorithm
        self.assertRaises(Exception, create_new_cache, 2, 1, 'custom', 'Not a function')
        # replacement_algorithm not specified
        self.assertRaises(Exception, create_new_cache, 2, 1, 'custom')
        # 4 % 3 != 0
        self.assertRaises(Exception, create_new_cache, 4, 3, 'LRU')
        # 'WrongStrategy' does not exist
        self.assertRaises(Exception, create_new_cache, 4, 3, 'WrongStrategy')

    def test_LRU_cache_hit_and_miss(self):
        """
        Testing the LRU cache for cache hits and misses
        """
        cache = create_new_cache(4, 2, 'LRU')

        # Inserting pairs into set 0
        cache.put(0, '0')
        cache.put(2, '2')
        self.assertEqual(cache.get(0), (True, '0'))
        self.assertEqual(cache.get(2), (True, '2'))
        # After adding new entry, (0, '0') should be replaced as it was LRU
        cache.put(4, '4')
        self.assertEqual(cache.get(0), (False, None))

        # set 0 should still me empty
        self.assertEqual(cache.get(1), (False, None))
        cache.put(1, 'old')
        cache.put(1, 'new')
        self.assertEqual(cache.get(1), (True, 'new'))

    def test_MRU_cache_hit_and_miss(self):
        """
        Testing the MRU cache for cache hits and misses
        """
        cache = create_new_cache(4, 2, 'MRU')

        cache.put(0, '0')
        cache.put(2, '2')
        self.assertEqual(cache.get(0), (True, '0'))
        self.assertEqual(cache.get(2), (True, '2'))
        cache.print_contents()
        # After adding new entry, (2, '2') should be replaced as it was MRU
        cache.put(4, '4')
        cache.put(2, '4')
        cache.put(5, '4')
        cache.put(6, '4')
        cache.print_contents()
        # self.assertEqual(cache.get(2), (False, None))

        cache.put(1, 'old')
        cache.put(1, 'new')
        cache.print_contents()
        # self.assertEqual(cache.get(1), (True, 'old'))

    def test_wrong_key_value_type(self):
        """
        Testing LRU cache with wrong key and value types
        """
        lru_cache = create_new_cache(2, 2, 'LRU')
        mru_cache = create_new_cache(2, 2, 'MRU')

        # The first input should initialise the cache default (key, value) types to (int, string)
        lru_cache.put(0, '0')
        self.assertRaises(Exception, lru_cache.put, 0, 1)
        self.assertRaises(Exception, lru_cache.put, '0', '1')
        mru_cache.put(0, '0')
        self.assertRaises(Exception, mru_cache.put, 0, 1)

    def test_custom_replacement_algorithm(self):
        """
        Testing a custom replacement algorithm
        """
        def replacement_algorithm(current_set):
            # Replace the 2nd LRU entry
            lru_node = current_set.head.next.next
            current_set.remove(lru_node)
            del current_set.dic[lru_node.key]

        cache = create_new_cache(3, 3, 'custom', replacement_algorithm=replacement_algorithm)
        # Note that we need at least 2 entries in a set for this particular strategy to work
        cache.put(0, '0')
        cache.put(1, '1')
        cache.put(2, '2')
        # (1, '1') should be now replaced as it is the 2nd LRU entry
        cache.put(3, '3')
        self.assertEqual(cache.get(1), (False, None))
