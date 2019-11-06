# Set-Associative-Cache
Author: Jan Noszczyk

The Library was written in Python 3.7.4

This is a library implementing an N-way, Set-Associative-Cache.

The Cache exists entirely in memory. 

The interface is type-safe to keys and values of arbitrary type specified by the user. For a given cache instance, all keys must be of the same type and all values must also be of the same type.

Cache classes that use both LRU and MRU node replacement methods are provided by default. The user can also specify custom replacement methods.

To install the library, locate the directory and run

    pip install .



