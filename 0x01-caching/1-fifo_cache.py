#!/usr/bin/env python3
"""
1-fifo_cache implements a `FIFOCache` that inherits
from BaseCaching and is a caching system.
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """A cache mechanism implementing the FIFO eviction algorithm."""

    def put(self, key, item):
        """Insert item using a FIFO algo."""
        if key is None or item is None:
            return
        if BaseCaching.MAX_ITEMS == len(self.cache_data) and key not \
                in self.cache_data:
            first_key = list(self.cache_data.keys())[0]
            self.cache_data.pop(first_key)
            print("DISCARD: {}".format(first_key))

        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item."""
        if key is None:
            return None
        return self.cache_data.get(key)


if __name__ == "__main__":
    my_cache = FIFOCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    my_cache.put("F", "Mission")
    my_cache.print_cache()
