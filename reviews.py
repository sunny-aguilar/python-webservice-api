#!/usr/bin/env python3
#
#   A
#   a
#   a
#
#   Author:     Sandro Aguilar
#   Date:       April 15, 2020
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import requests

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)