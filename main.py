from flask import Flask, render_template, request
import random
import array as arr

a =[]
a.append("dsdj")
print (a)

a =[]
print (a)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
  
