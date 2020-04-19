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

files = os.listdir('data/feedback')
# print(files)

feedback = {}

for file in files:
    for line in file:
        field = line.strip()
        feedback[field] = field.strip()

print(feedback)
