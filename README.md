# HospLine
![image](https://user-images.githubusercontent.com/83456083/159140052-47a4e537-77d0-4a1d-a3d3-8dc665329a15.png)

## Introduction
Amidst the global pandemic, managing crowd has been one of the prime challenge of the government and various institution. That is where HospLine comes to the rescue.
HospLine is a webapp that allows you to join a queue virtually which leads to no gathering hence lesser people in Hospitals that enables health workers to have the essentials handy.

## What does the Project do?
- You will have to fill in your details in the given form and it will assign you a spot in the virtual queue.
- On submitting the form, you'll be directed to a new page where your position in the virtual queue will be displayed.
- It will also inform you about the number of people ahead of you in the queue.
- If someone ahead of you leaves the queue, then the data will be updated and displayed on your page in realtime.

## Installation / Usage
1. Clone this Repo using:
```
git clone git@github.com:mdarshad1000/Hosp-Line.git
```
3. Change to the repo directory:
```
cd Hosp-Line
``` 
5. If you want to use virtual environment (Recommended):
```
virtualenv HOSPENV && source HOSPENV/bin/activate
```
7. After that, install all the requirements
```
pip install -r requirements.txt
```
9. Create an 'auth.json' file in the 'Hosp-Line' directory and add
```
{
    "HOST" : "hostname",
    "DB" : "database name",
    "USER" : "username",
    "PASS" : "password",
    "port_id" : "port
}
```
6. Run __init__.py, this will create your database. (Make sure you've Postresql installed on your local system) 
7. Now you are good to go. Run app.py and visit 
```
http://localhost:5000/
```
in your browser.

## Contribution Guidelines
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
