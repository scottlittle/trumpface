from flask import Flask, render_template
app = Flask(__name__)

@app.route("/") #this is called a decorator
def hello():
    return render_template("index.html",name="Ian")

@app.route("/trump") #this is called a decorator
def trump():
    return "donald"

if __name__ == "__main__":
    app.debug = True
    app.run()