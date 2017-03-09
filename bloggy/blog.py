#blog.py

from flask import Flask, render_template, request, session, flash, redirect, url_for, g
import sqlite3
from functools import wraps

# configuration
DATABASE = 'blog.db'

#Adding login static info for user login
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = '\x9e\xb7\xed\x1e\x18\x08\xe2O\x88|\x1d\x83j\xb4\xd2\xc5d0!\x07\xb4\xe6T\x0b'

app = Flask(__name__)

# pulls in app confirguration by looking for UPPERCASE variables
app.config.from_object(__name__) # this variabel is bringing in oru DATABASE variable

#function used for connecting to the database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

#THIS TESTS TO SEE IF THE USER IS LOGGED IN OR NOT, IF NOT DON'T DISPLAY OUR POSTS
def login_required(test):
    @wraps(test)
    def wrap (*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash("You need to login first.")
            return redirect(url_for("login"))
    return wrap
    
# template.routing
@app.route('/', methods = ["GET","POST"])                  
def login():
    error = None
    if request.method == 'POST': 
        if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Credentials. Please try again'
            #If the user has been authenticated then we show them the index.html or /main 
        else:
            session['logged_in'] = True
            return redirect(url_for('main'))
    return render_template('login.html', error=error)

@app.route('/main')
@login_required
def main():
    g.db = connect_db()
    cur = g.db.execute("select * from posts") # Here we get all of our data inside our database
    posts = [dict(title=row[0],post=row[1]) for row in cur.fetchall()] # Here we place data into a dictionary for display onto the page
    g.db.close() #Here we close our connection
    return render_template('index.html', posts=posts)

@app.route('/add', methods = ['POST'])
@login_required
def add():
    title = request.form["title"]
    post = request.form["post"]
    if not title or not post:
        flash("All fields are required. Please try again")
        return redirect(url_for("main"))
    else:
        g.db = connect_db()
        g.db.execute("insert into posts(title,post) values (?,?)", [request.form["title"], request.form['post']])
        g.db.commit()
        g.db.close()
        flash("Nre Entry was successfully posted!")
        return redirect(url_for("main"))

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    flash("You were logged out")
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(debug=True)