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
feedback = {}

for file in files:
    with open('data/feedback/'+file, 'r') as current_file:
    # f = open('data/feedback/' + file)
        for line in current_file:
            field = line.strip()
            print(field)
            feedback[field] = field.strip()

# print(feedback)
