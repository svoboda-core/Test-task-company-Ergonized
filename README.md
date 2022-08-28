# test task from ergonized
---
### Task: write a python script that automatically creates a discord account and logs in to a new authorization token with headers “authorization”
---
### Wash away:
* the script is guilty of receiving email and nickname from the command line<br>
* password is generated automatically<br>
* confirmation of the mail is not required<br>
---
### Check out:
* responsible for creating a face record and turning it into the command row token after login
---
To run the script, you need:
Create virtual sharpening:
### `python -m venv venv`

Activation of virtual sharpening:
### `venv\Scripts\activate`

Install the required deposi:
### `pip install -r requirements.txt`

In the hcaptcha.py file, replace 'APIKEY' with the API key from the 2Captcha service

Run script:
### `python main.py`
