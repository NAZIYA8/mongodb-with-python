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
        logger.info("Creating collection student.")
        col = db.student
        if col.drop():
            logger.info('Deleted existing collection')
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
        result = db.student.find()
        for data in result:
            logger.info(data)
        logger.info("Showed all documents\n")
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
            logger.info(i)
        logger.info("count\n")
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
            logger.info(i)
        logger.info("\n")
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
            logger.info(i)
        logger.info("minimum\n")
    except Exception as err:
        logger.error(err)

def max_func():
    """
        Description: 
            This function is used to get maximum score.
    """
    try:
        result = db.student.aggregate([{ '$group' : { "_id" :'$user', 'Maximum_score': {'$max':'$score'}}}])
        for i in result:
            logger.info(i)
        logger.info("maximum\n")
    except Exception as err:
        logger.error(err)

def avg_func():
    """
        Description: 
            This function is used to get the average score.
    """
    try:
        result = db.student.aggregate([{ '$group' : { "_id" :'$user', 'Average_score': {'$avg':'$score'}}}])
        for i in result:
            logger.info(i)
        logger.info("average\n")
    except Exception as err:
        logger.error(err)

if __name__ == "__main__":
    
    host = os.environ.get("HOST")
    port = os.environ.get("PORT")
    client = MongoClient(host,int(port))
    db = client.school
    create_collection()
    insert_multiple_doc()
    show_all()
    count_func()
    sum_func()
    min_func()
    max_func()
    avg_func()