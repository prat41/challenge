"""Routines associated with the application data.
"""

from flask import jsonify
import json
courses = {}


def load_data():
    """Load the data from the json file.
    """
    with open('json/course.json') as f:
        data = json.load(f)
        print(type(data))
        courses["data"] = data

    return courses
