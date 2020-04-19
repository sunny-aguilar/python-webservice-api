#!/usr/bin/env python3
#
#   A
#   a
#   a
#
#   Author:     Sandro Aguilar
#   Date:       April 15, 2020
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import os
import requests
import json

x = requests.get('https://w3schools.com/python/demopage.htm')

# print(x.headers)

files = os.listdir('data/feedback/')
# print(files)
field_names = ['title', 'name', 'date', 'feedback']
index = 0
feedback_list = []
feedback = {'title':'', 'name':'', 'date': '', 'feedback':''}

for file in files:
    with open('data/feedback/'+file, 'r+') as current_file:
    # f = open('data/feedback/' + file)
        for line in current_file:
            field = line.strip()
            # print(line)
            feedback[field_names[index]] = field
            index += 1
        
        # serialize data using json
        with open('feedback_list.json', 'w') as serial_feedback:
            # serialize Python object into json notation
            feedback_jason = json.dumps(feedback)
            # send data to API
            response = requests.post('http://', data = feedback_jason)

            # check data results and response code
            print(feedback_jason)
            print(response.status_code)

        # reset index
        index = 0
