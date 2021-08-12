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
        

if __name__ == "__main__":
    
    
    create_collection()
    