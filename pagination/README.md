# Pagination

This project covers how to paginate a dataset (`Popular_Baby_Names.csv`):

- with simple `page` and `page_size` parameters
- with hypermedia metadata (HATEOAS)
- in a deletion-resilient manner

## Files

| File | Description |
| --- | --- |
| `0-simple_helper_function.py` | `index_range(page, page_size)` returns a `(start, end)` tuple of indexes for a 1-indexed page. |

## Requirements

- Ubuntu 20.04 LTS, Python 3.9
- `pycodestyle` 2.5.*
- All modules and functions documented and type-annotated
