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

def show_all():
    """
        Description: 
            This function is used to display all the documents
            in the collection.
    """
    try:
        result = db.student.find()
        for data in result:
            print(data)
        print("Showed all documents\n")
    except Exception as err:
        logger.error(err)

def count_func():
    """
        Description: 
            This function is used to count the total subjects.
    """
    try:
        result = db.student.aggregate([{ '$group' : { "_id" :'$user', 'Total_subject': {'$sum':1}}}])
        for i in result:
            print(i)
        print("\n")
    except Exception as err:
        logger.error(err)

def sum_func():
    """
        Description: 
            This function is used to get the total scores.
    """
    try:
        result = db.student.aggregate([{ '$group' : { "_id" :'$user', 'Total_score': {'$sum':'$score'}}}])
        for i in result:
            print(i)
        print("\n")
    except Exception as err:
        logger.error(err)

def min_func():
    """
        Description: 
            This function is used to get the minimum score
    """
    try:
        result = db.student.aggregate([{ '$group' : { "_id" :'$user', 'Minimum_score': {'$min':'$score'}}}])
        for i in result:
            print(i)
        print("\n")
    except Exception as err:
        logger.error(err)


if __name__ == "__main__":
    
    create_collection()
    insert_multiple_doc()
    show_all()
    count_func()
    sum_func()
    min_func()