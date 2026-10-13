#!/usr/bin/env python3
"""Module with a function that changes the topics of a school document."""


def update_topics(mongo_collection, name, topics):
    """Change all topics of the school documents matching the given name.

    The mongo_collection argument is the pymongo collection object, name is
    the school name to update and topics is the list of topics to set.
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
