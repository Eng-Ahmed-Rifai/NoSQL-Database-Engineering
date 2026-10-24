"""
NoSQL Aggregation Pipeline and CRUD Engine.
Author: Eng. Ahmed Rifai
"""
from pymongo import MongoClient
import json

def get_aggregation_pipeline():
    return [
        {"$match": {"status": "active"}},
        {"$group": {
            "_id": "$category",
            "total_items": {"$sum": 1},
            "avg_latency_ms": {"$avg": "$latency"}
        }},
        {"$sort": {"total_items": -1}}
    ]

if __name__ == "__main__":
    print("NoSQL Aggregation Pipeline definition initialized successfully.")
    print(json.dumps(get_aggregation_pipeline(), indent=2))
