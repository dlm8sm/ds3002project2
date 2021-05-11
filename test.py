# test.py file in lambda function #

import requests

def call_pylenin(event=None, context=None):
    r = requests.get("https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi")
    rson = r.json()
    return rson
