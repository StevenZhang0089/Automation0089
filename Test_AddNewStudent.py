import requests
import json
import jsonpath

def test_add_student_data():
    API_URL= "http://thetestingworldapi.com/api/studentsDetails"
    f= open("B:/python/pytest01/TestCases/Test.jason",'r')
    json_requests =json.loads((f.read()))
    response= requests.post(API_URL,json_requests)
    print(response.text)

def test_get_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/82691"
    response = requests.get(API_URL)
    json_response = response.json()
    id = jsonpath.jsonpath(json_response, 'data.id')
    print(id)
    assert id[0] == 82691

def test_update_student_data():
    API_URL= "http://thetestingworldapi.com/api/studentsDetails/3034"
    f= open("B:/python/pytest01/TestCases/Test.jason",'r')
    json_requests =json.loads((f.read()))
    response= requests.put(API_URL,json_requests)
    print(response.text)

def test_get_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/82691"
    response = requests.get(API_URL)
    json_response = response.json()
    id = jsonpath.jsonpath(json_response, 'data.id')
    print(id)
    assert id[0] == 82691

def test_delete_student_data():
    API_URL= "http://thetestingworldapi.com/api/studentsDetails/3034"
    response= requests.delete(API_URL)
    print(response.text)

def test_get_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/82691"
    response = requests.get(API_URL)
    json_response = response.json()
    id = jsonpath.jsonpath(json_response, 'data.id')
    print(id)
    assert id[0] == 82691