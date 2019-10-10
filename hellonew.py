from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/hello/")
def hello():
  return "Hello Napier!!! :D"

@app.route("/goodbye/")
def goodbye():
  return "Goodbye cruel world :("

@app.route("/private")
def private():
  return redirect(url_for('login'))

@app.route("/login")
def login():
  return "GEEZ YER USERNAME AND PASSWORD"

@app.errorhandler(404)
def page_not_found(error):
  return "WHAT THE HELL ARE YOU DOING?", 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

