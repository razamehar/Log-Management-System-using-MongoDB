from pymongo import MongoClient
from dotenv import load_dotenv
import os
import time


def get_db():
    load_dotenv()

    user = os.getenv('USER')
    password = os.getenv('PASSWORD')
    host = os.getenv('HOST')

    while True:
        try:
            connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(user, password, host)

            # connect to mongodb server
            print("Connecting to mongodb server...")
            connection = MongoClient(connecturl)
            print("Connection established")

            return connection
        except Exception as e:
            print('Connecting to database failed.')
            print('Error:', e)
            print('Will try to reconnect in 2 seconds...')
            time.sleep(2)


def close_db(connection):
    if connection:
        print("Closing the connection...")
        connection.close()
    print("Connection closed.")