'''
@Author: Naziya
@Date: 2021-08-10
@Last Modified by: Naziya
@Last Modified : 2021-08-10
@Title : Program Aim is to perform sort operations.
'''

from LoggerFormat import logger
from pymongo import MongoClient

import os
from dotenv import load_dotenv
load_dotenv()

def create_collection():
    try:
        logger.info("Creating collection employee_details.")
        col = db.employee_details
        if col.drop():
            logger.info('Deleted existing collection')
        db.create_collection("employee_details")
    except Exception as err:
        logger.error(err)

def insert_multiple_doc():
    """
        Description: 
            This function is used to insert multiple documents to 
            the collection.
    """
    try:
        db.employee_details.insert_many([
        {
            "EmployeeNo" : "1",
            "FirstName" : "Dolly",
            "LastName": "Singh",
            "Age" : "27",
            "Salary": "30000"
        },
        {
            "EmployeeNo" : "2",
            "FirstName" : "Amit",
            "LastName": "Sharma",
            "Age" : "40",
            "Salary": "50000"
        },
        {
            "EmployeeNo" : "3",
            "FirstName" : "Komal",
            "LastName": "Pande",
            "Age" : "20",
            "Salary": "18000"
        },
        {
            "EmployeeNo" : "4",
            "FirstName" : "Ashima",
            "LastName": "Arora",
            "Age" : "25",
            "Salary": "28000"
        },
        {
            "EmployeeNo" : "5",
            "FirstName" : "Sneha",
            "LastName": "Joshi",
            "Age" : "30",
            "Salary": "45000"
        },
        {
            "EmployeeNo" : "6",
            "FirstName" : "Gautham",
            "LastName": "Deshpande",
            "Age" : "30",
            "Salary": "40000"
        }
        ])
        logger.info("Inserted multiple documents\n")
    except Exception as err:
        logger.error(err)


def show_all():
    """
        Description: 
            This function is used to display all the documents
            in the collection.
    """
    try:
        result = db.employee_details.find()
        for data in result:
            logger.info(data)
        logger.info("Showed all documents\n")
    except Exception as err:
        logger.error(err)


def sort_in_asc():
    """
        Description: 
            This function is used to sort in ascending order.
    """
    try:
        result = db.employee_details.find({}, {"Age":1, '_id':0}).sort("Age",1)
        for data in result:
            logger.info(data)
        logger.info("Successfully Sorted in ascending order\n")
    except Exception as err:
        logger.error(err)


def sort_in_desc():
    """
        Description: 
            This function is used to sort in descending order.
    """
    try:
        result = db.employee_details.find({}, {"FirstName":1, '_id':0}).sort("FirstName",-1)
        for data in result:
            logger.info(data)
        logger.info("Successfully Sorted in descending order\n")
    except Exception as err:
        logger.error(err)


def limit_func():
    """
        Description: 
            This function is used for limit function.
    """
    try:
        result = db.employee_details.find({}, {"FirstName":1,'_id':0}).limit(2)
        for data in result:
            logger.info(data)
        logger.info("Used limit function\n")
    except Exception as err:
        logger.error(err)


def skip_func():
    """
        Description: 
            This function is used for skip function.
    """
    try:
        result = db.employee_details.find({}, {"FirstName":1,'_id':0}).skip(2)
        for data in result:
            logger.info(data)
        logger.info("Used skip function\n")
    except Exception as err:
        logger.error(err)


if __name__ == "__main__":
    host = os.environ.get("HOST")
    port = os.environ.get("PORT")
    client = MongoClient(host,int(port))
    db = client.employee
    create_collection()
    insert_multiple_doc()
    show_all()
    sort_in_asc()
    sort_in_desc()
    limit_func()
    skip_func()
    