# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 17:13:20 2021

@author: AVINASH
"""

import pymongo

# mongo uri
MONGO_URI = "mongodb+srv://avinashlocal:3tHej8I3Fcdmt8np@cluster0.wzvo0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

class conn:
    def __init__(self):
        # to refer to a particular collection in db
        self.status = 1
        self.maindb_client = pymongo.MongoClient(MONGO_URI, connect=False)
        self.db_client = self.maindb_client.atm
        
    def get_conn(self, collection):
        """ Gets mongodb connection object and returns it"""
        try:
            client = self.db_client[collection]
        except:
            # set status as 0 to indicate client couldn't be made
            self.status = 0
            return None, False
        
        return client, True
    def close(self):
        self.maindb_client.close()
        