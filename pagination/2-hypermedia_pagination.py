#!/usr/bin/env python3
"""Hypermedia pagination module for a dataset of popular baby names."""
import csv
import math
from typing import Dict, List, Optional, Tuple, Union


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple with the start and end indexes for a given page.

    Page numbers are 1-indexed, so page 1 starts at index 0. The end index
    is exclusive, matching Python list slicing semantics.
    """
    start: int = (page - 1) * page_size
    end: int = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the server with an empty cached dataset."""
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
        """Return the requested page of the dataset as a list of rows.

        Both arguments must be integers greater than 0. An empty list is
        returned when the page is out of range for the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()
        if start >= len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[
            str, Union[int, List[List], Optional[int]]]:
        """Return a dictionary of pagination data with hypermedia metadata.

        The dictionary holds the page size, current page, page data, next
        and previous page numbers (None when absent) and the total pages.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }
