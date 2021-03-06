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
import os
from dotenv import load_dotenv
load_dotenv()

def create_collection():
    try:
        logger.info("Creating collection student_scores.")
        col = db.student_scores
        if col.drop():
            logger.info('Deleted existing collection')
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
        result = db.student_scores.find()
        for data in result:
            logger.info(data)
        logger.info("Showed all documents\n")
    except Exception as err:
        logger.error(err)

def single_field_index():
    """
        Description:  
            This function is used to create single field index.
    """
    logger.info('Creating index....')
    try:
        db.student_scores.create_index("name")
        logger.info("Single field Index created\n")
        for index in db.student_scores.list_indexes():
            logger.info(index)
    except Exception as err:
        logger.error(err)


def dropping_index():
    """
        Description: 
            This function is used to drop index.
    """
    logger.info('Dropping index....')
    try:
        db.student_scores.drop_index('name_1')
        logger.info("Index dropped\n")
        for index in db.student_scores.list_indexes():
            logger.info(index)
    except Exception as err:
        logger.error(err)

def compound_indexing():
    """
        Description: 
            This function is used to create a compound index.
    """
    logger.info('Creating index....')
    try:
        db.student_scores.create_index([("name", pymongo.DESCENDING),
                             ("subject", pymongo.ASCENDING)])
        logger.info("Compound Index created\n")
        for index in db.student_scores.list_indexes():
            logger.info(index)
    except Exception as err:
        logger.error(err)

if __name__ == "__main__":
    
    host = os.environ.get("HOST")
    port = os.environ.get("PORT")
    client = MongoClient(host,int(port))
    db = client.students
    create_collection()
    insert_multiple_doc()
    show_all()
    single_field_index()
    dropping_index()
    compound_indexing()