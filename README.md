# simple-flask-api-framework

This library is to be use to make simple rest application using flask

> falskapp.py is main file which understands URL and invoke proper action

> api route must be <:host>/api/<:classname>/<:param>

How this will work?
Let's take some example
User class (Example)
- To manage users in application, there is a class named User
- To access that class methods through api first select http method
- Note: each class will support only 4 methods ['GET','POST','PUT','DELETE']
- To get user list, api endpoint should be /api/user (http method GET)
- To get particular user, api endpoint should be /api/user/1

This application also shows firebase admin auth, so that data can be fetched from firebase and processed
- Go to Google console
- Create project
- Add service key from left side bar
- Replace key file in key/ directory

To change information in apis, change properties in Info() class
- Open info.py
- Make appropriate changes

----------------

How to use?
1. Clone the package
2. install dependencies

How to extend?
1. This project is made to create APIs using flask framework 
2. No need to hardcode routes and define functions each time
3. This works fast development kit
4. This project helps to keep code modular and automic
5. For each process you can add a class with get, post, put and delete methods which will be directly accessible from api endpoints
6. You can design classes and structure them as MC if required
7. Database hasn't used in this framework but can be added, fork this repository to add more functions

Contribute in development
1. Being opensource this project is open for contributions
2. Fork this repository and add appropeiate changes
3. For any question mail me to naikrahulda@gmail.com 

Try locally
1. export FLASK_APP=flaskapp.py
2. export FLASK_ENV=development
3. python -m flask run
