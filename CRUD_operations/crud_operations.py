'''
@Author: Naziya
@Date: 2021-08-09
@Last Modified by: Naziya
@Last Modified : 2021-08-09
@Title : Program Aim is to perform CRUD operations.
'''

from LoggerFormat import logger
from pymongo import MongoClient
client = MongoClient('localhost',27017)

db = client.test

def create_collection():
    try:
        print("Creating collection students.")
        col = db.students
        if col.drop():
            print('Deleted existing collection')
        db.create_collection("students")
    except Exception as err:
        logger.error(err)

def insert_one_doc():
    try:
        db.students.insert_one(
        {
            "StudentNo" : "1",
            "FirstName" : "Kinjal",
            "LastName": "Shah",
            "Age" : "10"
        })
    except Exception as err:
        logger.error(err)


if __name__ == "__main__":
    create_collection()
    insert_one_doc()
    print("Inserted one document")