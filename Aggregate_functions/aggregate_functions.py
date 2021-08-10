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

db = client.school


def create_collection():
    try:
        print("Creating collection student.")
        col = db.student
        if col.drop():
            print('Deleted existing collection')
        db.create_collection("student")
    except Exception as err:
        logger.error(err)

def insert_multiple_doc():
    """
        Description: 
            This function is used to insert multiple documents to 
            the collection.
    """
    try:
        db.student.insert_many([
            {'user':'Kinjal',"subject":'Database','score':80},
            {'user':'Dolly',"subject":'Javascript','score':90},
            {'user':'Dolly',"subject":'Database','score':85},
            {'user':'Kinjal',"subject":'Javascript','score':75},
            {'user':'Dolly',"subject":'DataScience','score':60},
            {'user':'Kinjal',"subject":'DataScience','score':95}
        ])
        print("Inserted multiple documents\n")
    except Exception as err:
        logger.error(err)


if __name__ == "__main__":
    
    create_collection()
    insert_multiple_doc()