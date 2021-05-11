# test.py file in lambda function #
import requests
import csv
import json
import os
import MySQLdb


HOST = 'project2-rds.cynlolhiptpy.us-east-1.rds.amazonaws.com'
USER = 'mowski'
PASS = os.environ.get('RDS_PASS')
db=MySQLdb.connect(host=HOST,user=USER,passwd=PASS,db="project2-rds")


def call_pylenin(event=None, context=None):
    r = requests.get("https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi")
    rson = r.json()
    # get json data from api
    factor = rson['factor']
    # factor value from api
    pi = rson['pi']     
    # pi value from api
    time = rson['time']
    # time value from api
    
    return INSERT INTO `API_DATA`(`factor`, `pi`, `time`) VALUES ('factor','pi','time')
