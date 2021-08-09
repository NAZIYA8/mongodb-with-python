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

def insert_multiple_doc():
    try:
        db.students.insert_many([
        {
            "StudentNo" : "2",
            "FirstName" : "Dolly",
            "LastName": "Singh",
            "Age" : "17"
        },
        {
            "StudentNo" : "3",
            "FirstName" : "Amit",
            "LastName": "Sharma",
            "Age" : "40"
        },
        {
            "StudentNo" : "4",
            "FirstName" : "Komal",
            "LastName": "Pande",
            "Age" : "12"
        },
        {
            "StudentNo" : "5",
            "FirstName" : "Ashima",
            "LastName": "Arora",
            "Age" : "15"
        },
        {
            "StudentNo" : "6",
            "FirstName" : "Sneha",
            "LastName": "Joshi",
            "Age" : "13"
        },
        {
            "StudentNo" : "7",
            "FirstName" : "Virat",
            "LastName": "Chauhan",
            "Age" : "16"
        },
        {
            "StudentNo" : "8",
            "FirstName" : "Gautham",
            "LastName": "Deshpande",
            "Age" : "16"
        }
        ])
    except Exception as err:
        logger.error(err)

if __name__ == "__main__":
    create_collection()
    insert_one_doc()
    print("Inserted one document")
    insert_multiple_doc()
    print("Inserted multiple documents")