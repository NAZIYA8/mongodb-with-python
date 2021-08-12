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

def insert_multiple_doc():
    """
        Description: 
            This function is used to insert multiple documents to 
            the collection.
    """
    try:
        db.orders.insert_many([
            { '_id': 1, 'cust_id': "Kinjal",  'price': 25, 'items': [ { 'sku': "oranges", 'qty': 5, 'price': 2.5 }, { 'sku': "apples", 'qty': 5, 'price': 2.5 } ]},
            { '_id': 2, 'cust_id': "Kinjal",  'price': 70, 'items': [ { 'sku': "oranges", 'qty': 8, 'price': 2.5 }, { 'sku': "chocolates", 'qty': 5, 'price': 10 } ]},
            { '_id': 3, 'cust_id': "Dolly",  'price': 50, 'items': [ { 'sku': "oranges", 'qty': 10, 'price': 2.5 }, { 'sku': "pears", 'qty': 10, 'price': 2.5 } ] },
            { '_id': 4, 'cust_id': "Dolly",  'price': 25, 'items': [ { 'sku': "oranges", 'qty': 10, 'price': 2.5 } ] },
            { '_id': 5, 'cust_id': "Dolly",  'price': 50, 'items': [ { 'sku': "chocolates", 'qty': 5, 'price': 10 } ]},
            { '_id': 6, 'cust_id': "Samar", 'price': 35, 'items': [ { 'sku': "carrots", 'qty': 10, 'price': 1.0 }, { 'sku': "apples", 'qty': 10, 'price': 2.5 } ]},
            { '_id': 7, 'cust_id': "Samar",  'price': 25, 'items': [ { 'sku': "oranges", 'qty': 10, 'price': 2.5 } ]},
            { '_id': 8, 'cust_id': "Pranay", 'price': 75, 'items': [ { 'sku': "chocolates", 'qty': 5, 'price': 10 }, { 'sku': "apples", 'qty': 10, 'price': 2.5 } ] },
            { '_id': 9, 'cust_id': "Pranay",  'price': 55, 'items': [ { 'sku': "carrots", 'qty': 5, 'price': 1.0 }, { 'sku': "apples", 'qty': 10, 'price': 2.5 }, { 'sku': "oranges", 'qty': 10, 'price': 2.5 } ]},
            { '_id': 10, 'cust_id': "Pranay",  'price': 25, 'items': [ { 'sku': "oranges", 'qty': 10, 'price': 2.5 } ] }
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
        result = db.orders.find()
        for data in result:
            print(data)
        print("Showed all documents\n")
    except Exception as err:
        logger.error(err)


if __name__ == "__main__":
    
    create_collection()
    insert_multiple_doc()
    show_all()
  