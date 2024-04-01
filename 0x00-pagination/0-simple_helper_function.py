#!/usr/bin/env python3
"""Write a function named index_range that takes
two integer arguments page and page_size.

The function should return a tuple of size two containing a start index
and an end index corresponding to the range of indexes to return
in a list for those particular pagination parameters.
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """computes start and end index for a page."""
    end = page * page_size
    start = end - page_size

    return (start, end)
