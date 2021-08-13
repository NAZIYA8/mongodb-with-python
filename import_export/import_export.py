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

db.emp_details.insert_many([
        {"EmployeeNo" : "1","FirstName" : "Dolly","LastName": "Singh","Age" : "27","Salary": "30000",'Gender':'Female'},
        {"EmployeeNo" : "2","FirstName" : "Amit","LastName": "Sharma","Age" : "40","Salary": "50000",'Gender':'Male'},
        {"EmployeeNo" : "3","FirstName" : "Komal","LastName": "Pande","Age" : "20","Salary": "18000",'Gender':'Female'},
        {"EmployeeNo" : "4","FirstName" : "Ashima","LastName": "Arora","Age" : "25","Salary": "28000",'Gender':'Female'},
        {"EmployeeNo" : "5","FirstName" : "Sneha","LastName": "Joshi","Age" : "30","Salary": "45000",'Gender':'Female'},
        {"EmployeeNo" : "6","FirstName" : "Gautham","LastName": "Deshpande","Age" : "30","Salary": "40000",'Gender':'Male'}
        ])
logger.info("Inserted Multiple Documents\n")

result = db.emp_details.find()
for data in result:
    logger.info(data)
logger.info("Showed all documents\n")

cursor = col.find()
mongo_docs = list(cursor)

logger.info("total docs:")
logger.info(len(mongo_docs))



