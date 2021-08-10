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



if __name__ == "__main__":
    
    create_collection()
    