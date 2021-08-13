'''
@Author: Naziya
@Date: 2021-08-13
@Last Modified by: Naziya
@Last Modified : 2021-08-13
@Title : Program Aim is to import and export to csv, json and html.
'''


from LoggerFormat import logger
from pymongo import MongoClient
import pandas
import time
import json

client = MongoClient('localhost',27017)
db = client.test3

logger.info("Creating collection emp_details")
col = db.emp_details
if col.drop(): 
    logger.info('Deleted existing collection')
db.create_collection("emp_details")

