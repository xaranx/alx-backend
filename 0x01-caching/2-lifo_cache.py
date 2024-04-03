#!/usr/bin/env python3
"""
2-lifo_cache implements a `LIFOCache` that inherits
from BaseCaching and is a caching system.
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """A cache mechanism implementing the LIFO eviction algorithm."""

    def put(self, key, item):
        """Insert item using a LIFO algo."""
        if key is None or item is None:
            return
        if BaseCaching.MAX_ITEMS == len(self.cache_data) and key not \
                in self.cache_data:
            last_key = list(self.cache_data.keys())[-1]
            self.cache_data.pop(last_key)
            print("DISCARD: {}".format(last_key))

        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item."""
        if key is None:
            return
        return self.cache_data.get(key)


if __name__ == "__main__":
    my_cache = LIFOCache()
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
