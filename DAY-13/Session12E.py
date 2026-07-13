from pymongo import MongoClient
from pymongo.server_api import ServerApi

class DBHelper:

    def __init__(self, db_name='gw2026'):
        uri = "mongodb+srv://dhruvjainofficials_db_user:Dhruv2311@cluster0.xsb4cxj.mongodb.net/?appName=Cluster0"
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.db = self.client[db_name]
        print('[DBHelper] Connection Created')

    def select_collection(self, collection_name='users'):
        self.collection = self.db[collection_name]
        print('[DBHelper] Collection Selected:"', collection_name)

    def save(self, document):
       inserted_id = self.collection.insert_one(document)
       print('[DBHelper] Document Saved. Id is:', inserted_id)
    
    def retrieve(self,condition=None):
        # result=self.collection.find()
        condition={'name: Dhruv Jain'}
        result=self.collection.find(condition)
        print("[DBHelper] Documents Retrieved, result is: ", result)

        for doc in result:
            print(doc) 
    def update(self, condition=None, document_to_update=None):
        result = self.collection.update_one(
            condition,
            {
                '$set': document_to_update
            }
        )
        print('[DBHelper] Document Updated', result)


    def delete(self, condition):
        result = self.collection.delete_one(condition)
        print('[DBHelper] Document Deleted', result)
