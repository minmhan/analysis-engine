'''
Date: 15/09/2026
Description: 
Author: Min Min
'''

from pymongo import MongoClient
import os
import gridfs
from bson.objectid import ObjectId

client = MongoClient('localhost', 27017)
db = client.ebookscollection
collection = db.ebooks