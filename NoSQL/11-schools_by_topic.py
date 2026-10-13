#!/usr/bin/env python3
"""Module with a function that finds the schools having a given topic."""


def schools_by_topic(mongo_collection, topic):
    """Return the list of school documents that have the given topic.

    The mongo_collection argument is the pymongo collection object and topic
    is the string searched in each school's list of topics.
    """
    return list(mongo_collection.find({"topics": topic}))
