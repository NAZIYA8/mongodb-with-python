'''
@Author: Naziya
@Date: 2021-08-09
@Last Modified by: Naziya
@Last Modified : 2021-08-09
@Title : Program Aim is to perform CRUD operations.
'''

from LoggerFormat import logger
from pymongo import MongoClient
client = MongoClient('localhost',27017)

db = client.test

def create_collection():
    try:
        print("Creating collection students.")
        col = db.students
        if col.drop():
            print('Deleted existing collection')
        db.create_collection("students")
    except Exception as err:
        logger.error(err)

def insert_one_doc():
    """
        Description: 
            This function is used to insert single document to the collection.
    """
    try:
        db.students.insert_one(
        {
            "StudentNo" : "1",
            "FirstName" : "Kinjal",
            "LastName": "Shah",
            "Age" : "10"
        })
        print("Inserted one document")
    except Exception as err:
        logger.error(err)

def insert_multiple_doc():
    """
        Description: 
            This function is used to insert multiple documents to 
            the collection.
    """
    try:
        db.students.insert_many([
        {
            "StudentNo" : "2",
            "FirstName" : "Dolly",
            "LastName": "Singh",
            "Age" : "17"
        },
        {
            "StudentNo" : "3",
            "FirstName" : "Amit",
            "LastName": "Sharma",
            "Age" : "40"
        },
        {
            "StudentNo" : "4",
            "FirstName" : "Komal",
            "LastName": "Pande",
            "Age" : "12"
        },
        {
            "StudentNo" : "5",
            "FirstName" : "Ashima",
            "LastName": "Arora",
            "Age" : "15"
        },
        {
            "StudentNo" : "6",
            "FirstName" : "Sneha",
            "LastName": "Joshi",
            "Age" : "13"
        },
        {
            "StudentNo" : "7",
            "FirstName" : "Virat",
            "LastName": "Chauhan",
            "Age" : "16"
        },
        {
            "StudentNo" : "8",
            "FirstName" : "Gautham",
            "LastName": "Deshpande",
            "Age" : "16"
        }
        ])
        print("Inserted multiple documents\n")
    except Exception as err:
        logger.error(err)

def show_one():
    """
        Description: 
            This function is used to display the single document.
    """
    try:
        print(db.students.find_one({"FirstName":"Ashima"}))
        print("Showed one document\n")
    except Exception as err:
        logger.error(err)

def show_all():
    """
        Description: 
            This function is used to display all the documents
            in the collection.
    """
    try:
        result = db.students.find()
        for data in result:
            print(data)
        print("Showed all documents\n")
    except Exception as err:
        logger.error(err)
    
def update_one_doc():
    """
        Description: 
            This function is used to update one document
            in the collection.
    """
    try:
        result = db.students.update_one(
            {"FirstName":"Amit"}, {"$set":{"LastName":"Shetty"}})
        print(result)
        print("Updated one document\n")
    except Exception as err:
        logger.error(err)

def update_multiple_doc():
    """
        Description: 
            This function is used to update multiple documents
            in the collection.
    """
    try:
        result = db.students.update_many(
            {"Age":"16"}, {"$set":{"LastName":"Aluwalia"}})
        for data in result:
            print(data)
        print("Updated multiple documents\n")
    except Exception as err:
        logger.error(err)

def remove_doc():
    """
        Description: 
            This function is used to remove document
            in the collection.
    """
    try:
        result = db.students.remove(
            {"LastName":"Shah"})
        print(result)
        print("Removed one document\n")
    except Exception as err:
        logger.error(err)

def save_doc():
    """ 
        Description: 
            This function is used to update the data if already existing
            and it inserts if its not existing
            in the collection.
    """
    try:
        result = db.students.save(
            {'StudentNo': '1', 'FirstName': 'Kinjal', 'LastName': 'Shah', 'Age': '10'})
        print(result)
        print("saved one document\n")
    except Exception as err:
        logger.error(err)

def AND_operation():
    """
        Description: 
            This function is used to perform AND operation
    """
    try:
        result = db.students.find({"FirstName":"Virat"},{"Age":"16"})
        for data in result:
            print(data)
        print("Successfully performed AND operation\n")
    except Exception as err:
        logger.error(err)

def OR_operation():
    """
        Description: 
            This function is used to perform OR operation
    """
    try:
        result = db.students.find(
            {
            "$or":[{"FirstName":"Sneha"},{"Age":"16"}]
            }
            )
        for data in result:
            print(data)
        print("Successfully performed OR operation\n")
    except Exception as err:
        logger.error(err)

def AND_OR_operation():
    """
        Description: 
            This function is used to perform combination of AND and OR
    """
    try:
        result = db.students.find(
            {
            "FirstName":"Dolly","$or":[{"Age":"40"},{"Age":"17"}]
            }
            )
        for data in result:
            print(data)
        print("Successfully performed combination of AND and OR operation\n")
    except Exception as err:
        logger.error(err)

def comparison_operators():
    """
        Description: 
            This function is used for comparison operators
    """
    try:
        result = db.students.find({"Age":{"$gt":"15"}})
        for data in result:
            print(data)
        print("Displayed Age greater than 15\n")

        result = db.students.find({"Age":{"$lt":"15"}})
        for data in result:
            print(data)
        print("Displayed Age less than 15\n")

        result = db.students.find({"Age":{"$gte":"16"}})
        for data in result:
            print(data)
        print("Displayed Age greater than equal to 16\n")

        result = db.students.find({"Age":{"$lte":"12"}})
        for data in result:
            print(data)
        print("Displayed Age less than equal to 12\n")

        result = db.students.find({"Age":{"$ne":"16"}})
        for data in result:
            print(data)
        print("Displayed Age not equal to 16\n")


    except Exception as err:
        logger.error(err)


if __name__ == "__main__":
    create_collection()
    insert_one_doc()
    insert_multiple_doc()
    show_one()
    show_all()
    update_one_doc()
    show_all()
    update_multiple_doc()
    show_all()
    remove_doc()
    show_all()
    save_doc()
    show_all()
    AND_operation()
    OR_operation()
    AND_OR_operation()
    comparison_operators()