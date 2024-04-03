#!/usr/bin/env python3
"""
4-mru-cache implements a `MRUCache` that inherits
from BaseCaching and is a caching system.
"""
from typing import List
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """A cache mechanism implementing the MRU eviction algorithm."""
    mru_keys: List[str] = []

    def put(self, key, item):
        """Insert item using a MRU algo."""
        if key is None or item is None:
            return
        if BaseCaching.MAX_ITEMS == len(self.cache_data):
            if key not in self.cache_data.keys():
                queue_key = type(self).mru_keys[-1]
                self.cache_data.pop(queue_key)
                self.dequeue(queue_key)
                print("DISCARD: {}".format(queue_key))

        self.cache_data[key] = item
        self.shift(key)

    def get(self, key):
        """Retrieve an item."""
        if key is None or key not in self.cache_data.keys():
            return
        self.shift(key)

        return self.cache_data.get(key)

    def shift(self, key):
        """Shift key to end of the queue."""
        self.dequeue(key)
        self.enqueue(key)

    def dequeue(self, key):
        """Remove key from queue."""
        if key in type(self).mru_keys:
            type(self).mru_keys.remove(key)

    def enqueue(self, key):
        """Add key to queue."""
        type(self).mru_keys.append(key)


if __name__ == "__main__":
    my_cache = MRUCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    print(my_cache.get("B"))
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
    my_cache.put("H", "H")
    my_cache.print_cache()
    my_cache.put("I", "I")
    my_cache.print_cache()
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
