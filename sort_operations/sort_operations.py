'''
@Author: Naziya
@Date: 2021-08-10
@Last Modified by: Naziya
@Last Modified : 2021-08-10
@Title : Program Aim is to perform sort operations.
'''

from LoggerFormat import logger
from pymongo import MongoClient

from LoggerFormat import logger
from pymongo import MongoClient
client = MongoClient('localhost',27017)

db = client.employee


def create_collection():
    try:
        print("Creating collection employee_details.")
        col = db.employee_details
        if col.drop():
            print('Deleted existing collection')
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
        print("Inserted multiple documents\n")
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
            print(data)
        print("Showed all documents\n")
    except Exception as err:
        logger.error(err)

if __name__ == "__main__":
    
    create_collection()
    insert_multiple_doc()
    show_all()
    