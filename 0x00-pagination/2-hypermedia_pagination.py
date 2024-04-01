#!/usr/bin/env python3
"""Implements a simple pagination mechanism for in the Server class"""
from typing import Any, Dict, List, Tuple
import csv
import math
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets a paginated set from the dataset."""
        assert isinstance(page, int)
        assert isinstance(page_size, int)

        assert page > 0
        assert page_size > 0

        paged: Tuple[int, int] = index_range(page, page_size)
        return self.dataset()[paged[0]: paged[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Get fully-formed paginated content."""
        assert isinstance(page, int)
        assert isinstance(page_size, int)

        assert page > 0
        assert page_size > 0

        paged: Tuple[int, int] = index_range(page, page_size)
        paged_data = self.dataset()[paged[0]: paged[1]]

        data_size = len(paged_data)
        next_page = None if (
            page * page_size) >= len(self.dataset()) else page + 1
        prev_page = None if page == 1 else page - 1
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            "page_size": data_size,
            "page": page,
            "data": paged_data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }


if __name__ == "__main__":
    server = Server()

    print(server.get_hyper(1, 2))
    print("---")
    print(server.get_hyper(2, 2))
    print("---")
    print(server.get_hyper(100, 3))
    print("---")
    print(server.get_hyper(3000, 100))
