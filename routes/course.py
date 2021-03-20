"""Routes for the course resource.
"""

import json
from run import app
from flask import request,jsonify
from http import HTTPStatus
import data
import datetime

course_data = data.load_data()

@app.route("/course/<int:id>", methods=['GET'])
def get_course(id):
    """Get a course by id.

    :param int id: The record id.
    :return: A single course (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------   
    1. Bonus points for not using a linear scan on your data structure.
    """
    # YOUR CODE HERE
    for i in course_data['data']:
        if i['id'] == id:
            return i

    return {"message": "Course {} does not exist".format(id)}


@app.route("/course", methods=['GET'])
def get_courses():
    """Get a page of courses, optionally filtered by title words (a list of
    words separated by commas".

    Query parameters: page-number, page-size, title-words
    If not present, we use defaults of page-number=1, page-size=10

    :return: A page of courses (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    ------------------------------------------------------------------------- 
    1. Bonus points for not using a linear scan, on your data structure, if
       title-words is supplied
    2. Bonus points for returning resulted sorted by the number of words which
       matched, if title-words is supplied.
    3. Bonus points for including performance data on the API, in terms of
       requests/second.
    """
    # YOUR CODE HERE
    search_queery = request.args.get('titlewords')
    page_size = request.args.get('page-size')
    page_number = request.args.get('page-number')

    # print(search_queery)
    # print((search_queery).split(','))
    li = []
    for i in course_data['data']:
        if any(map(lambda s : s in i['title'].lower(), search_queery.split(','))):
            li.append(i)

    return {"list":li}
        # if search_queery in i['title'].lower():
        # #     return i





@app.route("/course", methods=['POST'])
def create_course():
    """Create a course.
    :return: The course object (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    1. Bonus points for validating the POST body fields
    """
    # YOUR CODE HERE
    date_created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_updated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # title, image_path, price, on_discount, discount_price, description
    title = request.json['title']
    image_path = request.json['image_path']
    price = request.json['price']
    on_discount = request.json['on_discount']
    discount_price = request.json['discount_price']
    description = request.json['description']
    created_data = {}
    # if len(title) < 5 and len(title) > 100:
    #     return {"message" : "title length should not be less than 5 or greater than 100"}
    # else:
    #     created_data['title'] =







    li = ["date_created","date_updated","title", "image_path", "price", "on_discount", "discount_price", "description"]
    li2 = [date_created, date_updated, title, image_path, price, on_discount, discount_price, description]
    return dict(zip(li,li2))








@app.route("/course/<int:id>", methods=['PUT'])
def update_course(id):
    """Update a a course.
    :param int id: The record id.
    :return: The updated course object (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    1. Bonus points for validating the PUT body fields, including checking
       against the id in the URL

    """
    # YOUR CODE HERE


@app.route("/course/<int:id>", methods=['DELETE'])
def delete_course(id):
    """Delete a course
    :return: A confirmation message (see the challenge notes for examples)
    """
    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    None
    """
    # YOUR CODE HERE

