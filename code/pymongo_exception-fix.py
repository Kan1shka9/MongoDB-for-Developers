#!/usr/bin/env python
import pymongo

# Do not need to import sys

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.test
users = db.users

doc = {'firstname':'Kanishka', 'lastname':'sunnam'}
print doc
print "about to insert the document"

try:
    users.insert_one(doc)
except Exception as e:
    print "insert failed:", e

print doc
print "inserting again"
doc = {'firstname':'Kanishka', 'lastname':'sunnam'}

try:
    users.insert_one(doc)
except Exception as e:
    print "second insert failed:", e

print doc

