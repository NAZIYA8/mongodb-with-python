'''
@Author: Naziya
@Date: 2021-08-11
@Last Modified by: Naziya
@Last Modified : 2021-08-11
@Title : Program Aim is to perform map reduce
'''

from LoggerFormat import logger
from pymongo import MongoClient
client = MongoClient('localhost',27017)
from bson.code import Code

db = client.test2

def create_collection():
    try:
        print("Creating collection orders")
        col = db.orders
        if col.drop():
            print('Deleted existing collection')
        db.create_collection("orders")
    except Exception as err:
        logger.error(err)



if __name__ == "__main__":
    
    create_collection()
    
  