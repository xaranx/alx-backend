#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            # truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10):
        """better pagination mechanism."""
        idx_data = self.indexed_dataset()

        assert index < len(idx_data)

        out = {
            "index": index,
            "data": [],
            "page_size": 0,
            "next_index": 0,
        }

        n_count = 0
        found_idx = False

        for k, v in idx_data.items():
            if n_count >= page_size:
                break
            if k >= index and found_idx is False:
                found_idx = True
            if found_idx is True:
                out["data"].append(v)
                out["page_size"] += 1
                out['next_index'] = k+1
                n_count += 1

        return out
