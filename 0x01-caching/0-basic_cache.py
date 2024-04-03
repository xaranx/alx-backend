#!/usr/bin/python3
"""
0-basic-cache.py implements a class `BasicCache` that
inherits from `BaseCaching` and is a caching system.
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A basic cache datastructure."""

    def put(self, key, item):
        """Inserts an item into the cache using a simple caching algo."""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the cache using a simple caching algo."""
        if key is None:
            return
        return self.cache_data.get(key, None)
