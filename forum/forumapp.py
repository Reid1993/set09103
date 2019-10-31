from flask import Flask, render_template
app = Flask(__name__)

@app.route("/home/")
def home():
    return render_template("base.html"), 200

@app.route("/about/")
def about():
    return render_template("about.html"), 200

if __name__ == ("__main__"):
    app.run(host="0.0.0.0", debug=True)
