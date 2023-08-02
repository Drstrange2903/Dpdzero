# Dpdzero

It is an API Backend system Developed  as per the Assignment :
The framework used here is Flask as it is easy to write and test APis in it
The Coding language used here is Python
The database used here is MySql


To run the code you have first to set up three things:
1. Virtual environment for Flask to run
Download the Virtual environment using pip install virtualenv
using the env create an env with the name you want and activate ./env/Scripts/activate
once set add the app.py 

2. Database connection: I have MySQL as a database, make a schema according to Data and connect it to the flask

3. set up Postman to send requests we wanted with data, some of them are mentioned below:-

The API will be accessible at http://127.0.0.1:5000/¹. Postman requests can now be utilized to test the API and carry out actions on users.

1. To create a new user, send a POST request to http://127.0.0.1:5000/users with JSON
data containing "name" and other field details.
2. To fetch all users, send a GET request to 'http://127.0.0.1:5000/users`.
3. To fetch a specific user by ID, send a GET request to 'http://127.0.0.1:5000/users/1
(replace 1 with the desired user ID).
4. To update a user by ID, send a PUT request to http://127.0.0.1:5000/users/1` (replace
1 with the desired user ID) with JSON data containing "name" and other details
5. To delete a user by ID, send a DELETE request to http://127.0.0.1:5000/users/1
(replace 1 with the desired user ID).



