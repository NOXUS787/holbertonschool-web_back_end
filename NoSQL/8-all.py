#!/usr/bin/env python3
"""Module with a function that lists all documents in a collection."""


def list_all(mongo_collection):
    """Return a list of all documents in the given pymongo collection.

    An empty list is returned when the collection has no documents.
    """
    return list(mongo_collection.find())
