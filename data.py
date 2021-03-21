"""Routines associated with the application data.
"""

from flask import jsonify
import json
courses = {}


def load_data():
    """Load the data from the json file.
    """
    try:
        with open('json/course.json') as f:
            data = json.load(f)
            courses["data"] = data

    except Exception as e :
        print("Error : {}".format(e))

    return courses


