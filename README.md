CAR PRICE PREDICTION CHALLENGE

https://test-flask-app-a.herokuapp.com/

This repository consists of files required for end to end implementation and deployment of Machine Learning Car Price Prediction web application created with Flask and deployed on the Heroku platform.

Welcome, and thank you for opening this Project. This project contains :

1-Data :

1.1-RAW: contain the original data (not clean)

1.2-CURATED: in this floder you will find clean data

2-Src :

2.1-Jupyter NoteBook 'brief 7' & 'badewa analys' : 

Here, we read in our data set and doing some cleanning and analyses

2.2-App.py

is a flask web application which predicts car prices based on given independent features like 

2.3-Model.py

in this part we prepare the data (scaling dummies ..) then we train the linear regression model on 70% then we test on 30% of the data.
we use pickle to save the model

2.4- template and static/css :

you will find in this floders index.html style.css 

necessary files to build the graphical interface of the app

2.5- requirements.txt

this file contains the required packages and libraries to make the app 

2.6-some pkl file like model.pkl and scalerX.pkl ...

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280>](https://gunicorn.org) [<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=200>](https://scikit-learn.org/stable/) 




