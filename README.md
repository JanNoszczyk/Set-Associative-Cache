# Set-Associative-Cache
Author: Jan Noszczyk

The Library was written in Python 3.7.4

This is a library implementing a N-way, Set-Associative-Cache.

The Cache exists entirely in memory. 

The interface is type-safe to keys and values of arbitrary type specified by the user. 
For a given cache instance, all keys must be of the same type and all values must also be of the same type.

Cache classes that use both LRU and MRU node replacement methods are provided by default. 
The user can also specify custom replacement methods.

## Installation
To install the library, locate the directory and run
```bash
$ pip install .
```

## Usage
### Creating a Cache object
The create an object of the Cache class run the create_new_cache method

```python
create_new_cache(size, number_of_ways, strategy='LRU', replacement_algorithm=None)
```
`size` *(int)* The total number of cache entries

`number_of_ways` *(int)* Number of cache entries per set

`strategy` *(str)* Strategy to remove an entry from the cache set after its size limit has been exceeded. It can be either 
'LRU', 'MRU' or 'custom'.

`replacement_algorithm` *(function)* User defined node replacement method (Only used when `strategy='custom'`)

```python
# Example
from set_associative_cache.cache import create_new_cache
lru_cache = create_new_cache(2, 2, 'LRU')
```
Custom replacement algorithms should be defined as functions implementing a custom node removal method. 

The input `current_set` is the Cache set from which a node should be removed. It is of type *HashedLinkedList*, which 
implements a doubly linked list with dummy `head` and `tail` nodes. It also has a hashtable `dic` storing references to 
all nodes in the linked list for quick access. 

The linked list also has methods: `remove` which removes a specified node from the 
linked list, and `add` which adds a node at the end of the linked list.

Each *Node* object has attributes `key`, `value`, as well as `next` and `prev` linking it to other nodes.
```python
# Example showing the LRU replacement method
def replacement_algorithm(current_set):
    lru_node = current_set.head.next
    current_set.remove(lru_node)
    del current_set.dic[lru_node.key]
```
### Using a Cache object
Each Cache object has the following methods

`set(key, value)` Adds a new entry to the cache.

`get(key)` Retrieves a value from the cache for a specified key. If the key is present, it will also be placed at 
the beginning of the linked list.

`replace(current_set)` Removes an entry from the cache set after its capacity has been exceeded.

`print_contents()` Prints the current cache contents.

```python
# Example
>>> lru_cache = create_new_cache(2, 2, 'LRU')
>>> lru_cache.set(1, 'Val_1')
>>> lru_cache.set(2, 'Val_2')
>>> lru_cache.get(1)
(True, 'Val_1')
>>> lru_cache.set(3, 'Val_3')
>>> lru_cache.print_contents()
Set 0: (1, Val_1) (3, Val_3)
```
