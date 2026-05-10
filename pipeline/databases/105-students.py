#!/usr/bin/env python3
"""Python function that returns all students sorted by average score"""


def top_students(mongo_collection):
    """Returns all students sorted by avg_score"""
    return mongo_collection.aggregate([
        {"$students": {
            "name": 1,
            "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])
