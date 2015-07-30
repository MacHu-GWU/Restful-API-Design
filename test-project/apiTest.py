##encoding=utf-8


from pprint import pprint as ppt
import requests
import json

def prt(json_text):
    js = json.loads(json_text)
    print( json.dumps(js, sort_keys=True, indent=4, separators=("," , ": ")) )
    
# prt(requests.get("http://127.0.0.1:5000/").text)
# prt(requests.get("http://127.0.0.1:5000/people").text)

def create_example():
    requests.post("http://127.0.0.1:5000/people", data={"firstname": "barack", "lastname": "obama"})
    requests.post("http://127.0.0.1:5000/people", data={"firstname": "mitt", "lastname": "romney"})
    
# create_example()

def read_example():
#     prt(requests.get("http://127.0.0.1:5000/people").text)
#     prt(requests.get("http://127.0.0.1:5000/people/55a3db000080d448f8b68448").text)
    prt(requests.get("http://127.0.0.1:5000/people/obama").text)
    
# read_example()


prt(requests.get('http://127.0.0.1:5000/people?where={"firstname": "barack"}').text)
# prt(requests.get('http://127.0.0.1:5000/people?sort=-lastname').text)