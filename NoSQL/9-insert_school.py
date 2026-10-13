#!/usr/bin/env python3
"""Module with a function that inserts a new document in a collection."""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document built from kwargs and return its new _id.

    The mongo_collection argument is the pymongo collection object.
    """
    return mongo_collection.insert_one(kwargs).inserted_id
