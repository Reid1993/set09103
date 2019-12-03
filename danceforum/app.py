from flask import Flask, render_template, redirect, url_for, request, flash, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'Reid'
database = 'database.db'

with sqlite3.connect(database) as db:
    cursor = db.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS users(
        userID INTEGER PRIMARY KEY,
        email VARCHAR(100) NOT NULL,
        username VARCHAR(100) NOT NULL,
        password VARCHAR(100) NOT NULL);
        """)

    cursor.execute(""" CREATE TABLE IF NOT EXISTS posts(
        postID INTEGER PRIMARY KEY,
        creatorID VARCHAR(100) NOT NULL,
        title VARCHAR(255) NOT NULL,
        content TEXT NOT NULL,
        pageID INTEGER NOT NULL,
        FOREIGN KEY (creatorID) REFERENCES users (username));
        """)

@app.route("/")
@app.route("/home/")
def index():
    with sqlite3.connect(database) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM posts WHERE postID=1")
        posts = [dict(postID=row[0], creatorID=row[1], title=row[2], content=row[3]) for row in cur.fetchall()]
    return render_template("base.html", posts=posts)

@app.route("/register/", methods=["GET", "POST"])
def reg():
    error = None
    if request.method == "POST":
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        with sqlite3.connect(database) as con:
            if not email:
                error = 'Email Required.'
            elif not username:
                error = 'Username Required.'
            elif not password:
                error = 'Password Required.'
            else:
                cur = con.cursor()
                cur.execute("INSERT INTO users (email,username,password) VALUES (?,?,?)",(email,username,password))
                con.commit()
                flash('Account has been created.')
                return redirect(url_for("log"))
    return render_template("register.html", error=error)
    con.close()
    
@app.route("/login/", methods=["GET", "POST"])
def log():
    error = None
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        with sqlite3.connect(database) as con:
            cur = con.cursor()
            finduser = ("SELECT * FROM users WHERE username = ? AND password = ?")
            cur.execute(finduser,[(username),(password)])
            results = cur.fetchall()
            if results:
                session.pop('user', None)
                session['user'] = request.form['username']
                #session['id'] = request.form['userID']
                return redirect(url_for("profile"))
            else:
                error = "Invalid Credentials. Please Try Again."
    return render_template("login.html", error=error)

@app.route("/logout/")
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/profile/")
def profile():
    if 'user' in session:
        with sqlite3.connect(database) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM posts WHERE creatorID=creatorID")
            posts = [dict(postID=row[0], creatorID=row[1], title=row[2], content=row[3]) for row in cur.fetchall()]
            #findposts = cur.execute("SELECT * FROM posts WHERE creatorID = ?", session['user'])
            #posts = cur.fetchall()
            if posts:
                return render_template("profile.html", posts=posts)
            else:
                msg = "You have no posts"
                return render_template("profile.html", msg=msg)
    else:
        flash('You must login to view your profile!')
    return redirect(url_for("log"))

@app.route("/addpost/", methods=["GET", "POST"])
def addpost():
    if 'user' in session:
        error = None
        if request.method == "POST":
            pageId = request.form.get('groupid')
            title = request.form['title']
            content = request.form['content']
            with sqlite3.connect(database) as con:
                cur = con.cursor()
                cur.execute("INSERT INTO posts (creatorID,pageID,title,content) VALUES (?,?,?,?)",(session['user'],pageId,title,content))
                con.commit()
                flash('Post has been created!')
        return render_template("add_posts.html")
        con.close()
    else:
        flash('You must log in to create a post!')
        return redirect(url_for("log"))

@app.route("/post/<string:postID>/")
def post(postID):
    with sqlite3.connect(database) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM posts WHERE postID=postID")
        posts = [dict(postID=row[0], creatorID=row[1], title=row[2], content=row[3]) for row in cur.fetchall()]
        print (posts)
    return render_template("post.html", postID=postID, posts=posts)

@app.route("/ukevents/")
def ukev():
    with sqlite3.connect(database) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM posts WHERE pageID=1")
        posts = [dict(postID=row[0], creatorID=row[1], title=row[2], content=row[3]) for row in cur.fetchall()]
    return render_template("ukevents.html", posts=posts)

@app.route("/europeanevents/")
def euev():
    with sqlite3.connect(database) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM posts WHERE pageID=2")
        posts = [dict(postID=row[0], creatorID=row[1], title=row[2], content=row[3]) for row in cur.fetchall()]
    return render_template("euroevents.html", posts=posts)

@app.route("/usaevents/")
def usaev():
    with sqlite3.connect(database) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM posts WHERE pageID=3")
        posts = [dict(postID=row[0], creatorID=row[1], title=row[2], content=row[3]) for row in cur.fetchall()]
    return render_template("usaevents.html", posts=posts)

@app.route("/djzone/")
def djz():
    with sqlite3.connect(database) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM posts WHERE pageID=4")
        posts = [dict(postID=row[0], creatorID=row[1], title=row[2], content=row[3]) for row in cur.fetchall()]
    return render_template("djzone.html", posts=posts)

@app.route("/producerzone/")
def proz():
    with sqlite3.connect(database) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM posts WHERE pageID=5")
        posts = [dict(postID=row[0], creatorID=row[1], title=row[2], content=row[3]) for row in cur.fetchall()]
    return render_template("prozone.html", posts=posts)

@app.route("/thestudio/")
def stu():
    with sqlite3.connect(database) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM posts WHERE pageID=6")
        posts = [dict(postID=row[0], creatorID=row[1], title=row[2], content=row[3]) for row in cur.fetchall()]
    return render_template("studio.html", posts=posts)

@app.route("/chat/")
def muchat():
    with sqlite3.connect(database) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM posts WHERE pageID=7")
        posts = [dict(postID=row[0], creatorID=row[1], title=row[2], content=row[3]) for row in cur.fetchall()]
    return render_template("muchat.html", posts=posts)

@app.route("/recommendations/")
def murec():
    with sqlite3.connect(database) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM posts WHERE pageID=8")
        posts = [dict(postID=row[0], creatorID=row[1], title=row[2], content=row[3]) for row in cur.fetchall()]
    return render_template("murec.html", posts=posts)

@app.route("/reviews/")
def murev():
    with sqlite3.connect(database) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM posts WHERE pageID=9")
        posts = [dict(postID=row[0], creatorID=row[1], title=row[2], content=row[3]) for row in cur.fetchall()]
    return render_template("murev.html", posts=posts)
   
if __name__ == ("__main__"):
    app.run(host="0.0.0.0")