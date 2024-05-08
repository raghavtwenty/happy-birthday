"""
Application Name: HBD Fireworks
Designed and Developed by: Raghava, Kendriya Vidyalaya, Coimbatore. [2021]
Github : @raghavtwenty
Created On: 2 August 2021
Last Modified On: May 7, 2024
Version Info: 1.0
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Importing Required Libraries
from flask import Flask, render_template
from flask import request, jsonify
from requests import get

import requests
import json


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Routes
app = Flask(__name__)


# Default Home Route
@app.route("/")
def home():
    return render_template("Hello.html")


# Fireworks Route
@app.route("/Boom", methods=["POST"])
def greet():

    # Initalization
    name = request.form.get("Name")
    name_s = name.strip()
    name_l = name_s.lower()

    # Counter
    VC_File = open("Visitor_Count.txt", "r")
    Counter = VC_File.read()
    Counter = int(Counter)
    Counter += 1

    # Added new counter value to text file
    VCI_File = open("Visitor_Count.txt", "w")
    VCI_File.write(str(Counter))

    return render_template("Boom.html", NAME=name_l.upper(), VISITOR_COUNT=Counter)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main
if __name__ == "__main__":
    app.run(debug=True)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
