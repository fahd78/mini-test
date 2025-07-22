import requests

def before_feature(context, feature):
    requests.post("http://localhost:5001/testing/reset")
