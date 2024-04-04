#!/usr/bin/env python3
"""
3-lfu-cache implements a `LFUCache` that inherits
from BaseCaching and is a caching system.
"""
from typing import Dict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """A cache mechanism implementing the LFU eviction algorithm."""

    def __init__(self) -> None:
        super().__init__()
        self.lfu_dict: Dict[str, int] = {}
        self.least_k = ""

    def put(self, key, item):
        """Insert item using a LFU algo."""
        if key is None or item is None:
            return
        if BaseCaching.MAX_ITEMS == len(self.cache_data):
            if key not in self.cache_data.keys():
                kk = self.least_k if self.least_k  \
                    else list(self.cache_data.keys())[0]
                self.cache_data.pop(kk)
                self.dequeue(kk)
                print("DISCARD: {}".format(kk))

        self.cache_data[key] = item
        self.enqueue(key)
        self.update_lfu()

    def get(self, key):
        """Retrieve an item."""
        if key is None or key not in self.cache_data.keys():
            return
        self.enqueue(key)
        self.update_lfu()

        return self.cache_data.get(key)

    def dequeue(self, key):
        """Remove key from queue."""
        if key not in self.lfu_dict.keys():
            return
        del self.lfu_dict[key]

    def enqueue(self, key):
        """Add key to queue."""
        v = self.lfu_dict.get(key, 0)
        self.lfu_dict[key] = v + 1

    def update_lfu(self):
        """update value of the lru item."""
        min_val = 1
        min_k = ""
        rev_keys = list(self.lfu_dict.keys())
        rev_keys.reverse()

        for k in rev_keys:
            if self.lfu_dict[k] <= min_val:
                min_val = self.lfu_dict[k]
                min_k = k

        self.least_k = min_k


if __name__ == "__main__":
    my_cache = LFUCache()
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
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
    my_cache.put("L", "L")
    my_cache.print_cache()
    my_cache.put("M", "M")
    my_cache.print_cache()
