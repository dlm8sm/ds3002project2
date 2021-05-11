# test.py file in lambda function #
import requests
import csv

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
    list = [factor, pi, time]
    
    return list
