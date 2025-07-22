import requests

def before_feature(context, feature):
    requests.post("http://localhost:5000/testing/reset")
