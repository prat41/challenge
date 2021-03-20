"""Routes for the course resource.
"""

import json
from run import app
from flask import request,jsonify
from http import HTTPStatus
import data
import datetime

course_data = data.load_data()


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:

        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1


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
    result = []

    f_data  = {}

    if page_size:
        f_data = course_data
    else:
        page_size = 10

    if page_number:
        f_data = course_data
    else:
        page_number = 1


    if search_queery:
        for i in course_data['data']:
            if any(map(lambda s: s in i['title'].lower(), search_queery.split(','))):
                li.append(i)
        f_data['data'] = li
    else:
        f_data = course_data

    if int(page_size) > 0 :
        result = f_data['data'][(int(page_number)-1) * int(page_size) : (int(page_number)-1) * int(page_size) + int(page_size)]

    v = (len(f_data['data'])) / (int(page_size))
    u = int(v)
    if v > u:
        u = u+1


    return {"data": result,
            "metadata": {
                        "page_count": u ,
                        "page_number": page_number,
                        "page_size": page_size,
                        "record_count": len(f_data['data'])
            }
    }








    # def pagesize():
    #     if int(str(page_size)) == 10:
    #         return course_data
    #     else:
    #         return {"message":"Page size not found"}
    #
    # def pagenumber():
    #     if int(str(page_number)) == 1:
    #         return course_data
    #     else:
    #         return {"message":"Page Number not found"}


    # li = []
    # for i in course_data['data']:
    #     if any(map(lambda s : s in i['title'].lower(), search_queery.split(','))):
    #         li.append(i)
    #









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

