#Demonstration of QA by Chris Chalfoun (Pointfit)

import requests
import getpass #python built-in library to mask password

url = "https://example.com/login" #change to valid address

valid_email = input("Input a valid email address: ")  
valid_password = getpass.getpass(prompt='Input a valid password: ', stream=None)

invalid_email = input("Input an invalid email address: ")
invalid_password = getpass.getpass(prompt='Input an invalid password: ', stream=None)

def send_request(email, password):
    data = {
        "email": email,
        "password": password
    }
    #make sure to get valid json format from website

    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.post(url, json=data, headers=headers)

    return response.status_code, response.json()

def test_login(email, password, expected_result):
    status_code, response_json = send_request(email, password)

    print(f"Testing login for {email}")
    print(f"Expected Result: {expected_result}")
    print(f"Status Code: {status_code}")
    print(f"Response Text: {response_json}\n")

    if response_json.get("resultCode") == "AUTHENTICATION_FAILURE":
        print("Authentication failed as expected.\n")
    elif response_json.get("resultCode") == "HUMAN_VERIFICATION_FAILED": #this text was found through manual testing first
        print("Authentication failed due to reCaptcha.\n")
    else:
        print("Login was successful as expected.\n")

test_login(valid_email, valid_password, expected_result="valid") #test with valid credentials

test_login(invalid_email, invalid_password, expected_result="invalid") #test with invalid credentials

#todo: add proxy support
