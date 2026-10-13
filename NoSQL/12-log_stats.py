#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB."""
from pymongo import MongoClient


def log_stats(mongo_collection):
    """Print the total logs, the count per HTTP method and status checks.

    The mongo_collection argument is the pymongo collection holding the
    Nginx logs, with documents that have method and path attributes.
    """
    print("{} logs".format(mongo_collection.count_documents({})))
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = mongo_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))
    status = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print("{} status check".format(status))


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    log_stats(client.logs.nginx)
