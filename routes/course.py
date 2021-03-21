"""Routes for the course resource.
"""

import json
from run import app
from flask import request,jsonify
from http import HTTPStatus
import data
import datetime

course_data = data.load_data()


def binary_search(data, id):
    low = 0
    length = len(data) - 1
    middle = 0
    while low <= length:

        middle = (length + low) // 2

        if data[middle]['id'] < id:
            low = middle + 1

        elif data[middle]['id'] > id:
            length = middle - 1

        else:
            return data[id - 1]

    return {"message": "Course {} does not exist".format(id)}

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

    return jsonify(binary_search(course_data['data'], id))

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
    search_query = request.args.get('titlewords')
    page_size = request.args.get('page-size')
    page_number = request.args.get('page-number')
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


    if search_query:
        for i in course_data['data']:
            if any(map(lambda s: s in i['title'].lower(), search_query.split(','))):
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
    title = request.json['title']
    image_path = request.json['image_path']
    price = request.json['price']
    on_discount = request.json['on_discount']
    discount_price = request.json['discount_price']
    description = request.json['description']
    created_data = {}

    li = []



    if len(title) in range(5,101):
        created_data['title'] = title
    else:
        li.append(False)

    if type(price) == float or type(price) == int:
        created_data['price'] = float(price)
    else:
        li.append(False)

    if type(on_discount) == bool:
        created_data['on_discount'] = on_discount
    else:
        li.append(False)

    if len(image_path) <= 100:
        created_data["image_path"] = image_path
    else:
        li.append(False)

    if len(description) <= 255:
        created_data["description"] = description
    else:
        li.append(False)


    if all(li):
        created_data['id'] = len(course_data['data']) + 1
        created_data['date_created'] = date_created
        created_data['date_updated'] = date_updated

        # courses = {}
        # with open('json/course.json') as f:
        #     data = json.load(f)
        #     courses["data"] = data

        def write_json(data1, filename='json/course.json'):

            with open(filename, 'w') as f:
                json.dump(data1, f, indent=4)

        with open('json/course.json') as json_file:
            data1 = json.load(json_file)
            temp = data1
            # print(data1)
            # print("This is Temp", temp)
            y = created_data
            temp.append(y)
            # print("This appended",temp, end='\n\n\n')

        write_json(data1)
        # print(course_data['data'][195:200])
        course_data['data'] = data.load_data()['data']
        return jsonify(course_data['data'][created_data['id']-1])
    else:
        return {"message":"Error in Creating Course"}

    # course_data['data'].append(created_data)
    # with open('json/course.json', 'w') as outfile:
    #     json.dump(created_data, outfile)







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

    date_updated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    title = request.json['title']
    image_path = request.json['image_path']
    price = request.json['price']
    on_discount = request.json['on_discount']
    discount_price = request.json['discount_price']
    description = request.json['description']

    updated_data = {}
    li = []

    if len(title) in range(5, 101):
        updated_data['title'] = title
    else:
        li.append(False)

    if type(price) == float or type(price) == int:
        updated_data['price'] = float(price)
    else:
        li.append(False)

    if discount_price:
        updated_data['discount_price'] = int(discount_price)
    else:
        li.append(False)

    if type(on_discount) == bool:
        updated_data['on_discount'] = on_discount
    else:
        li.append(False)

    if len(image_path) <= 100:
        updated_data["image_path"] = image_path
    else:
        li.append(False)

    if len(description) <= 255:
        updated_data["description"] = description
    else:
        li.append(False)

    updated_data['date_updated'] = date_updated

    course_data['id']






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

