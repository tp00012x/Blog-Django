# ---- Flask Hello World App ===#

#import the Flask class from the flask package
from flask import Flask, render_template

#creating the application object for our project
app = Flask(__name__)

#error handling using DEBUG

app.config["DEBUG"] = True

#Static routing
#Using Decorators to link these functions to a url
#Using @ sign, we are declaring a decorator for our route
@app.route("/")
@app.route("/helloworld")

#Example of using a function which returns a string.
#This is what our @app.route is looking for when doing our routing.
def hello_world():
    return "Hello World DEBG"

#Dynamic routing
@app.route("/test/<search_query>")
def search(search_query):
    return search_query

#Dynamic royting using flask converter
@app.route("/integer/<int:value>")
def int_type(value):
    print value + 1
    return "correct"

@app.route("/float/<float:value>")
def float_type(value):
    print value + 1
    return "correct"

#dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
    print value
    return "correct" + value

#Calling Html
@app.route("/<string:page_name>/")
def index_type(page_name):
    return render_template("%s.html" % page_name)
    
#starting the development server using the flask run () built-in method
if __name__ == "__main__":
    app.run()