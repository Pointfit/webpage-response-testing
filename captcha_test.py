#Demonstration of QA by Chris Chalfoun (Pointfit)

import requests
import getpass #python built-in library to mask password

url = "https://example.com/login" #change to valid address

email = input("Enter your email address: ")  
password = getpass.getpass(prompt='Enter your password: ', stream=None)

def send_request(email, password):
    data = {
        "email": email,
        "password": password
    }
    #make sure to get valid json format from website

    headers = {
        'Content-Type': 'application/json', #the data being sent is in json format
    }

    response = requests.post(url, json=data, headers=headers) #data automatically formats into json string

    print(f"Status Code: {response.status_code}") #print outcome from website
    print(f"Response Text: {response.text}")

    if "recaptchaRequired" in response.text: #this text was found through manual testing first
        print("reCAPTCHA is active and blocking the login attempt.")
    else:
        print("No reCAPTCHA detected in the response.")

send_request(email, password)

#todo: threading, proxy test, list of emails/passwords

