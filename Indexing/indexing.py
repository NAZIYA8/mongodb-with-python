'''
@Author: Naziya
@Date: 2021-08-11
@Last Modified by: Naziya
@Last Modified : 2021-08-11
@Title : Program Aim is to perform indexing.
'''
import pymongo
from LoggerFormat import logger
from pymongo import MongoClient , ASCENDING,DESCENDING
client = MongoClient('localhost',27017)

db = client.students

def create_collection():
    try:
        print("Creating collection student_scores.")
        col = db.student_scores
        if col.drop():
            print('Deleted existing collection')
        db.create_collection("student_scores")
    except Exception as err:
        logger.error(err)

def insert_multiple_doc():
    """
        Description: 
            This function is used to insert multiple documents to 
            the collection.
    """
    try:
        db.student_scores.insert_many([
            {'name':'Kinjal',"subject":'Maths','score':92},
            {'name':'Dolly',"subject":'Physics','score':87},
            {'name':'Samar',"subject":'Maths','score':99,'notes':'Excellent'},
            {'name':'Komal',"subject":'English','score':78},
            {'name':'Pranay',"subject":'History','score':65,'notes':'Adequate'}
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
        result = db.student_scores.find()
        for data in result:
            print(data)
        print("Showed all documents\n")
    except Exception as err:
        logger.error(err)


if __name__ == "__main__":
    
    
    create_collection()
    insert_multiple_doc()
    show_all()